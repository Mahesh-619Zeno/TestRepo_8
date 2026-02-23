import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

class LockManager:
    def task_one(self):
        with lock_a:
            with lock_b:
                print("Task one")

    def task_two(self):
        with lock_b:
            with lock_a:
                print("Task two")
