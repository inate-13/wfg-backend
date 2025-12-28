import asyncio
import logging
from datetime import datetime, timezone
from pymongo.errors import DuplicateKeyError

from app.db.mongo import get_db

logger = logging.getLogger(__name__)


async def process_transaction(transaction_id: str):
    db = get_db()
    logger.info(f"Started processing transaction {transaction_id}")

    await asyncio.sleep(30)

    db.transactions.update_one(
        {"transaction_id": transaction_id},
        {
            "$set": {
                "status": "PROCESSED",
                "processed_at": datetime.now(timezone.utc)
            }
        }
    )

def create_transaction_if_not_exists(payload: dict) -> bool:
    db = get_db()
    try:
        db.transactions.insert_one({
            **payload,
            "status": "PROCESSING",
            "created_at": datetime.now(timezone.utc),
            "processed_at": None
        })
        return True
    except DuplicateKeyError:
        logger.info(f"Duplicate transaction received: {payload['transaction_id']}")
        return False
