import random
import time
from datetime import datetime, timedelta
import uuid
from threading import Thread


def create_and_process_payment(order_id: str, amount: float, payment_method: str, payment_db: dict):
    payment_id = str(uuid.uuid4())
    new_payment = {
        "order_id": order_id,
        "amount": amount,
        "payment_method": payment_method,
        "payment_status": "Created",
        "payment_id": payment_id
    }
    
    payment_db["payments"].append(new_payment)
    
    thread = Thread(target=verify_and_process_payment, args=(payment_id, payment_db))
    thread.start()

    return {
        "status": "Created",
        "message": "Payment created and is being verified.",
        "payment": new_payment,
        "payment_id": payment_id
    }

def verify_and_process_payment(payment_id: str, payment_db: dict):
    time.sleep(10)
    for payment in payment_db["payments"]:
        if payment["payment_id"] == payment_id:
            payment["payment_status"] = "Verifying"
            time.sleep(10)
            payment_status = random.choice(["Success", "Failed"])
            payment["payment_status"] = payment_status
            break

def check_payment_status(payment_id: str, payment_db: dict):
    for payment in payment_db["payments"]:
        if payment["payment_id"] == payment_id:
            return {
                "status": "Success",
                "payment_status": payment["payment_status"],
                "payment": payment
            }
    return {
        "status": "Failed",
        "message": "Payment ID not found"
    }