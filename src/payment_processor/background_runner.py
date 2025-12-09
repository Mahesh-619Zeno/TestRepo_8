import threading
from .payment_processor import run_in_background

def start(payments, n=3):
    for _ in range(n):
        t = threading.Thread(target=run_in_background, args=(payments,))
        t.daemon = True
        t.start()
