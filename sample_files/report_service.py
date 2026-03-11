from typing import List, Dict
from datetime import datetime


class Transaction:
    def __init__(self, id: str, user_id: str, amount: float, created_at: datetime):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.created_at = created_at


class TransactionRepository:

    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transactions(self, user_id: str) -> List[Transaction]:
        result = []

        for transaction in self.transactions:
            if transaction.user_id == user_id:
                result.append(transaction)

        return result


class ReportService:

    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    def generate_report(self, user_id: str) -> Dict:

        transactions = self.repo.get_transactions(user_id)

        total_amount = 0
        monthly_data = {}

        for transaction in transactions:

            total_amount += transaction.amount

            month = transaction.created_at.strftime("%Y-%m")

            if month not in monthly_data:
                monthly_data[month] = 0

            monthly_data[month] += transaction.amount

        report = {
            "user_id": user_id,
            "total_amount": total_amount,
            "monthly_data": monthly_data,
            "transaction_count": len(transactions)
        }

        return report

    def filter_transactions(self, transactions: List[Transaction], start_date: datetime):

        filtered = []

        for transaction in transactions:
            if transaction.created_at >= start_date:
                filtered.append(transaction)

        return filtered