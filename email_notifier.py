import os
import smtplib
import threading
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("email_notifier")

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "noreply@example.com"
SENDER_PASS = os.getenv("SMTP_SENDER_PASS")

def send_email(recipient, subject, body):
  with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASS)
    message = f"From: {SENDER_EMAIL}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
    server.sendmail(SENDER_EMAIL, recipient, message)
    logger.info(f"Email sent to {recipient}")

def background_notifications(recipients):
    def task():
        for r in recipients:
            try:
                send_email(r, "System Alert", "This is a test alert.")
                time.sleep(1)
            except Exception as e:
                logger.exception(f"Failed to send email to {r}")
    t = threading.Thread(target=task, daemon=True)
    t.start()

def main():
    recipients = ["user1@example.com", "user2@example.com"]
    background_notifications(recipients)
    logger.info("Notifications scheduled")

if __name__ == "__main__":
    main()