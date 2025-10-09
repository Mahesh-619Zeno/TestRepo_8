from src.payment_processor.payment_processor import PaymentProcessor, run_in_background

if __name__ == "__main__":
    payments = [{"user": "u1", "amount": 10}, {"user": "u2", "amount": 20}]
    p = PaymentProcessor()
    p.handle_bulk_payments(payments)
    run_in_background(payments)
