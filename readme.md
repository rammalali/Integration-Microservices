# E-Commerce Microservices Application

This project is a FastAPI-based microservices application that manages various components of an e-commerce system including:
- **Accounting**: Handles financial transactions and summaries.
- **Payment Gateway**: Manages payment processing.
- **Delivery Service**: Handles logistics and shipping.
- **Email Service**: Sends notifications and confirmations.

## Prerequisites

Ensure the following are installed on your machine:
- **Docker** and **Docker Compose** (if you are using the Docker setup)
- **Python 3.9+**
- **FastAPI** and **Uvicorn** as the server

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository

2. **Install Python dependencies**:
   ```bash
    pip install -r requirements.txt

3. **Environment variables: Create a `.env` file for sensitive credentials like email**:
    ```bash
    EMAIL_USER=your-email@gmail.com
    EMAIL_PASSWORD=your-email-password

4. **Run with Docker**:
    ```bash
    docker-compose up
5. **Run without Docker: Start the FastAPI app using `uvicorn`:**
    ```bash
    uvicorn app:app --reload


## API Endpoints

### 1. **Accounting System**
- **POST `/record_transaction/`**: Record a new financial transaction.
  - **Body**:
    ```json
    {
      "transaction_id": "txn_001",
      "amount": 100.0,
      "date": "2024-10-22",
      "description": "Payment for order 123"
    }
    ```
  - **Response**:
    - If the transaction ID is new, the transaction is recorded and returned.
    - If the transaction ID already exists, a failure message is returned.

- **GET `/financial_summary/`**: Retrieve the financial summary (total sales and all transactions).

### 2. **Payment Gateway**
- **POST `/payment/`**: Create and process a payment.
  - **Body**:
    ```json
    {
      "order_id": "order_123",
      "amount": 100.0,
      "payment_method": "Credit Card"
    }
    ```
  - **Response**: The payment is created and is in the process of being verified and processed.

- **GET `/payment_status/{payment_id}`**: Poll the payment status based on `payment_id`.

### 3. **Delivery Service**
- **POST `/delivery/`**: Create, update, or get delivery info based on the `action` parameter.
  - **Body**:
    ```json
    {
      "action": "create",
      "order_id": "order_123",
      "delivery_address": "123 Main St",
      "carrier": "FedEx",
      "delivery_type": "Express"
    }
    ```
  - **Actions**:
    - **Create**: Creates a new delivery.
    - **Update**: Updates the delivery status with a new status.
    - **Get**: Retrieves delivery information based on the `order_id`.

- **GET `/delivery/?order_id={order_id}`**: Retrieve delivery information based on `order_id`.

### 4. **Email Service**
- **POST `/send_email/`**: Send an email with subject and body to a recipient.
  - **Body**:
    ```json
    {
      "receiver_email": "recipient@example.com",
      "subject": "Order Confirmation",
      "body": "Your order has been confirmed!"
    }
    ```
