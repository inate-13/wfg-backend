from pymongo import MongoClient, ASCENDING
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

_client: MongoClient | None = None
_db = None


def connect_to_mongo():
    global _client, _db

    _client = MongoClient(settings.mongo_uri)
    _db = _client[settings.db_name]

    _db.transactions.create_index(
        [("transaction_id", ASCENDING)],
        unique=True
    )

    logger.info("Connected to MongoDB")


def close_mongo_connection():
    global _client
    if _client:
        _client.close()
        logger.info("MongoDB connection closed")


def get_db():
    if _db is None:
        raise RuntimeError("MongoDB is not initialized")
    return _db
