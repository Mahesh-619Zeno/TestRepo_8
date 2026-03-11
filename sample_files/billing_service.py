from typing import List, Dict
from datetime import datetime


class Payment:
    def __init__(self, id: str, user_id: str, amount: float, method: str, created_at: datetime):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.method = method
        self.created_at = created_at


class PaymentRepository:

    def __init__(self):
        self.data: List[Payment] = []

    def add_payment(self, payment: Payment):
        self.data.append(payment)

    def get_payments(self, user_id: str) -> List[Payment]:
        items = []

        for p in self.data:
            if p.user_id == user_id:
                items.append(p)

        return items


class BillingService:

    def __init__(self, repo: PaymentRepository):
        self.repo = repo

    def create_payment(self, user_id: str, amount: float, method: str):

        obj = Payment(
            id=f"{user_id}-{datetime.utcnow().timestamp()}",
            user_id=user_id,
            amount=amount,
            method=method,
            created_at=datetime.utcnow()
        )

        self.repo.add_payment(obj)

        return obj

    def get_summary(self, user_id: str) -> Dict:

        payments = self.repo.get_payments(user_id)

        total = 0
        method_map = {}

        for payment in payments:

            total += payment.amount

            if payment.method not in method_map:
                method_map[payment.method] = 0

            method_map[payment.method] += payment.amount

        info = {
            "user_id": user_id,
            "total": total,
            "methods": method_map,
            "count": len(payments)
        }

        return info

    def cleanup(self, days: int):

        now = datetime.utcnow()
        new_list = []

        for p in self.repo.data:

            diff = (now - p.created_at).days

            if diff <= days:
                new_list.append(p)

        self.repo.data = new_list

    def convert(self, payments: List[Payment]) -> List[Dict]:

        result = []

        for p in payments:
            item = {
                "id": p.id,
                "amount": p.amount,
                "method": p.method,
                "time": p.created_at.isoformat()
            }

            result.append(item)

        return result