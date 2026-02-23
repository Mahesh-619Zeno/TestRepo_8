# api_handler.py

import json
import logging
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

logger = logging.getLogger("api")

class UserAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/user/"):
            user_id = self.path.split("/")[-1]
            self._handle_get_user(user_id)
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    def _handle_get_user(self, user_id):
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        query = f"SELECT id, name, email FROM users WHERE id = '{user_id}'"
        cur.execute(query)
        row = cur.fetchone()
        if row:
            self._set_headers(200)
            self.wfile.write(json.dumps({
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "User not found"}).encode())

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode())
        self._create_user(data)

    def _create_user(self, data):
        name = data.get("name")
        email = data.get("email")
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        conn.commit()
        self._set_headers(201)
        self.wfile.write(json.dumps({"status": "User created"}).encode())

def run(server_class=HTTPServer, handler_class=UserAPIHandler, port=8080):
    server = server_class(("", port), handler_class)
    server.serve_forever()

if __name__ == "__main__":
    run()
