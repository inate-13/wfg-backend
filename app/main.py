from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.mongo import connect_to_mongo, close_mongo_connection
from app.api.health import router as health_router
from app.api.webhooks import router as webhook_router
from app.api.transactions import router as transaction_router
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def startup_event():
    logger.info("Starting application")
    connect_to_mongo()


@app.on_event("shutdown")
def shutdown_event():
    close_mongo_connection()
    logger.info("Shutting down application")


app.include_router(health_router)
app.include_router(webhook_router)
app.include_router(transaction_router)
