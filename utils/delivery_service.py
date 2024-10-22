

def create_delivery(order_id: str, delivery_address: str, carrier: str, delivery_type: str, delivery_db: dict):
    new_delivery = {
        "order_id": order_id,
        "delivery_address": delivery_address,
        "carrier": carrier,
        "delivery_type": delivery_type,
        "status": "Pending"
    }
    
    delivery_db["deliveries"].append(new_delivery)
    
    return {
        "status": "Success",
        "message": "Delivery created successfully",
        "delivery": new_delivery
    }

def update_delivery_status(order_id: str, new_status: str, delivery_db: dict):
    for delivery in delivery_db["deliveries"]:
        if delivery["order_id"] == order_id:
            delivery["status"] = new_status
            return {
                "status": "Success",
                "message": "Delivery status updated",
                "delivery": delivery
            }
    
    return {
        "status": "Failed",
        "message": "Order ID not found"
    }

def get_delivery_info(order_id: str, delivery_db: dict):
    for delivery in delivery_db["deliveries"]:
        if delivery["order_id"] == order_id:
            return delivery
    
    return {
        "status": "Failed",
        "message": "Order ID not found"
    }
