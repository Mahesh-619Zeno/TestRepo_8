import os
import smtplib
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("email_notifier")

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "noreply@example.com")
SENDER_PASS = os.getenv("SENDER_PASS")  # MUST be provided through env var

if not SENDER_PASS:
    logger.warning("Environment variable SENDER_PASS is not set!")

MAX_WORKERS = 3

executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

# --------------------------------------------------------------------------- #
# Email utilities
# --------------------------------------------------------------------------- #

def send_email(recipient: str, subject: str, body: str):
    """Send an email with proper resource cleanup."""
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASS)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(SENDER_EMAIL, recipient, message)

        logger.info(f"Email sent to {recipient}")

    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {e}")
        raise
    finally:
        try:
            server.quit()
        except Exception:
            pass


def notify_many(recipients):
    """Send emails concurrently in a controlled thread pool."""
    futures = {
        executor.submit(send_email, r, "System Alert", "This is a test alert."): r
        for r in recipients
    }

    for future in as_completed(futures):
        recipient = futures[future]
        try:
            future.result()
        except Exception as e:
            logger.error(f"Notification failure for {recipient}: {e}")

# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    recipients = ["user1@example.com", "user2@example.com"]
    logger.info("Scheduling notifications...")
    notify_many(recipients)
    logger.info("Notification job finished.")

if __name__ == "__main__":
    main()
