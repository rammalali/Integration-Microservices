from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils.payment_gateway import create_and_process_payment, check_payment_status
from utils.accounting_system import record_transaction, get_financial_summary
from utils.delivery_service import create_delivery, update_delivery_status, get_delivery_info
from utils.email_service import send_email


accounting_db = {
    "transactions": [],
    "total_sales": 0.0
}

delivery_db = {
    "deliveries": []
}

payment_db = {
    "payments": []
}

app = FastAPI()


class Transaction(BaseModel):
    transaction_id: str
    amount: float
    date: str
    description: str

class DeliveryRequest(BaseModel):
    action: str
    order_id: str
    delivery_address: str = None
    carrier: str = None
    delivery_type: str = None
    status: str = None

class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    payment_method: str

@app.get("/delivery/")
def delivery_service(order_id: str):
    response = get_delivery_info(
        order_id=order_id,
        delivery_db=delivery_db
    )
    return response



@app.post("/record_transaction/")
def record_transaction_endpoint(transaction: Transaction):
    for t in accounting_db["transactions"]:
        if t["transaction_id"] == transaction.transaction_id:
            return {
                "status": "Failed",
                "message": "Transaction ID already exists",
                "transaction_id": transaction.transaction_id
            }
        
    response = record_transaction(
        transaction_id=transaction.transaction_id,
        amount=transaction.amount,
        date=transaction.date,
        description=transaction.description,
        accounting_db=accounting_db
    )
    return response

@app.get("/financial_summary/")
def get_financial_summary_endpoint():
    summary = get_financial_summary(accounting_db=accounting_db)
    return summary



@app.post("/delivery/")
def delivery_service(request: DeliveryRequest):
    if request.action == "create":
        if not request.delivery_address or not request.carrier or not request.delivery_type:
            raise HTTPException(status_code=400, detail="Missing required fields for creation.")
        response = create_delivery(
            order_id=request.order_id,
            delivery_address=request.delivery_address,
            carrier=request.carrier,
            delivery_type=request.delivery_type,
            delivery_db=delivery_db
        )
    
    elif request.action == "update":
        if not request.status:
            raise HTTPException(status_code=400, detail="Missing status for update.")
        response = update_delivery_status(
            order_id=request.order_id,
            new_status=request.status,
            delivery_db=delivery_db
        )

    elif request.action == "get":
        response = get_delivery_info(
            order_id=request.order_id,
            delivery_db=delivery_db
        )
    
    else:
        raise HTTPException(status_code=400, detail="Invalid action type.")
    
    return response

@app.get("/delivery/")
def delivery_get(order_id: str):
    response = get_delivery_info(
        order_id=order_id,
        delivery_db=delivery_db
    )
    return response


@app.post("/send_email/")
def send_email_endpoint(receiver_email: str, subject: str, body: str):
    smtp_server = "smtp.gmail.com"
    port = 465
    response = send_email(
        receiver_email=receiver_email,
        subject=subject,
        body=body,
        smtp_server=smtp_server,
        port=port
    )
    return response


@app.post("/payment/")
def payment_service(request: PaymentRequest):
    response = create_and_process_payment(
        order_id=request.order_id,
        amount=request.amount,
        payment_method=request.payment_method,
        payment_db=payment_db
    )
    return response

@app.get("/payment_status/{payment_id}")
def payment_status_service(payment_id: str):
    response = check_payment_status(
        payment_id=payment_id,
        payment_db=payment_db
    )
    return response
