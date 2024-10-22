

def record_transaction(transaction_id: str, amount: float, date: str, description: str, accounting_db: dict):
    new_transaction = {
        "transaction_id": transaction_id,
        "amount": amount,
        "date": date,
        "description": description
    }
    
    accounting_db["transactions"].append(new_transaction)
    accounting_db["total_sales"] += amount
    
    return {
        "status": "Success",
        "message": "Transaction recorded successfully",
        "transaction": new_transaction,
        "total_sales": accounting_db["total_sales"]
    }

def get_financial_summary(accounting_db: dict):
    return {
        "total_sales": accounting_db["total_sales"],
        "transactions": accounting_db["transactions"]
    }
