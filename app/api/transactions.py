from fastapi import APIRouter, HTTPException
from app.db.mongo import get_db
from app.models.transaction import TransactionResponse

router = APIRouter(prefix="/v1/transactions", tags=["Transactions"])

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: str):
    db = get_db()
    transaction = db.transactions.find_one(
        {"transaction_id": transaction_id},
        {"_id": 0}
    )

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction
