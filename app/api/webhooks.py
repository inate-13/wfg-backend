from fastapi import APIRouter, BackgroundTasks, status
import logging

from app.models.transaction import TransactionWebhookRequest
from app.services.transaction_service import (
    create_transaction_if_not_exists,
    process_transaction
)

router = APIRouter(prefix="/v1/webhooks", tags=["Webhooks"])
logger = logging.getLogger(__name__)


@router.post(
    "/transactions",
    status_code=status.HTTP_202_ACCEPTED
)
async def transaction_webhook(
    payload: TransactionWebhookRequest,
    background_tasks: BackgroundTasks
):
    """
    Receives transaction webhooks and processes them asynchronously.
    """

    inserted = create_transaction_if_not_exists(payload.dict())

    # Only trigger background processing if this is a new transaction
    if inserted:
        background_tasks.add_task(
            process_transaction,
            payload.transaction_id
        )

    return {"message": "Accepted"}
