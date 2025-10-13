# small helper functions (intentionally left simple)
def format_payment(p):
    return {"user": p.get("user"), "amount": p.get("amount")}
