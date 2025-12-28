**Transaction Webhook Service**

This project implements a backend service that receives transaction webhooks, acknowledges them immediately, and processes transactions asynchronously in the background.

The service is designed to be fast, idempotent, and reliable.

**Deployed Service URL** - https://wfg-backend-y095.onrender.com/

**Features**

Accepts transaction webhooks via HTTP

Responds immediately with 202 Accepted

Processes transactions asynchronously with a simulated delay

Prevents duplicate processing of the same transaction

Stores transaction status and timestamps

Exposes a health check and transaction status API

Deployed as a public API on the cloud

**Tech Stack**

Python

FastAPI

MongoDB

FastAPI BackgroundTasks

Uvicorn

Deployed on Render

**API Endpoints**
Health Check
GET /


Response:

{
  "status": "HEALTHY",
  "current_time": "2024-01-15T10:30:00Z"
}

Transaction Webhook
POST /v1/webhooks/transactions


Request body:

{
  "transaction_id": "txn_abc123def456",
  "source_account": "acc_user_789",
  "destination_account": "acc_merchant_456",
  "amount": 1500,
  "currency": "INR"
}


Behavior:

Always returns 202 Accepted

Responds immediately

Duplicate webhooks are ignored safely

Transaction Status
GET /v1/transactions/{transaction_id}


Returns the current status of the transaction (PROCESSING or PROCESSED).

**Instructions to Run Locally**
Prerequisites

Python 3.10 or higher

MongoDB (local or MongoDB Atlas)

**Setup**

Clone the repository

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


**Install dependencies:**

pip install -r requirements.txt


Create a .env file:

APP_NAME=transaction-webhook-service
ENV=local
MONGO_URI=mongodb://localhost:27017
DB_NAME=transactions_db


Run the service:

uvicorn app.main:app --reload


The service will be available at:

http://localhost:8000 locally 
and production deployed at  - https://wfg-backend-y095.onrender.com/ 


Swagger docs:

http://localhost:8000/docs

and production  at  -https://wfg-backend-y095.onrender.com/docs
