import time
import threading
import requests

class PaymentProcessor:
    def __init__(self):
        self.api_url = "https://payment.example.com/process"
        self.session = requests.Session()

    def process_payment(self, payment_data):
        response = requests.post(self.api_url, json=payment_data)
        if response.status_code == 200:
            print("Payment successful")
        else:
            print("Payment failed")

    def handle_bulk_payments(self, payments):
        for payment in payments:
            self.process_payment(payment)

def run_in_background(payments):
    for payment in payments:
        t = threading.Thread(target=PaymentProcessor().process_payment, args=(payment,))
        t.start()

if __name__ == "__main__":
    payments = [{"user": "u1", "amount": 10}, {"user": "u2", "amount": 20}]
    processor = PaymentProcessor()
    processor.handle_bulk_payments(payments)

    time.sleep(2)

    run_in_background(payments)
