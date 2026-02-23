import os
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, HTTPServer

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("upload_service")

UPLOAD_DIR = "uploads"
PORT = 8080
MAX_WORKERS = 5

os.makedirs(UPLOAD_DIR, exist_ok=True)

# Bounded thread pool
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

# --------------------------------------------------------------------------- #
# File utilities
# --------------------------------------------------------------------------- #

def save_file(filename: str, content: bytes) -> str:
    """Safely write file to disk."""
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(content)

    logger.info(f"Saved file: {path} ({len(content)} bytes)")
    return path


def process_file(path: str) -> None:
    """Business logic for processing the uploaded file."""
    time.sleep(1)  # Simulated work

    with open(path, "rb") as f:
        data = f.read()

    size = len(data)
    if size > 1000:
        raise ValueError(f"File too large: {size} bytes")

    logger.info(f"Processed file {os.path.basename(path)} ({size} bytes)")


def submit_background_job(path: str) -> None:
    """Submit file processing to worker pool."""
    future = executor.submit(process_file, path)

    def callback(f):
        try:
            f.result()
        except Exception as e:
            logger.error(f"Background worker failed: {e}")

    future.add_done_callback(callback)

# --------------------------------------------------------------------------- #
# HTTP Handler
# --------------------------------------------------------------------------- #

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length <= 0:
                self.send_error(400, "No content")
                return

            body = self.rfile.read(content_length)

            filename = f"upload_{int(time.time() * 1000)}.bin"
            path = save_file(filename, body)

            # Queue background processing
            submit_background_job(path)

            # Response
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"File uploaded successfully")
            logger.info("Upload request processed successfully")

        except Exception as e:
            logger.exception("Error handling POST request")
            self.send_error(500, str(e))

    def log_message(self, fmt, *args):
        # Prevent default noisy HTTP server logging
        logger.info("%s - %s" % (self.address_string(), fmt % args))

# --------------------------------------------------------------------------- #
# Server start
# --------------------------------------------------------------------------- #

def start_server():
    server = HTTPServer(("0.0.0.0", PORT), SimpleHandler)
    logger.info(f"Server running on port {PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down server...")
    finally:
        executor.shutdown(wait=True)
        server.server_close()
        logger.info("Server stopped.")

if __name__ == "__main__":
    start_server()
