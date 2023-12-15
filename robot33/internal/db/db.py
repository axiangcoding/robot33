import motor
from motor.motor_asyncio import AsyncIOMotorClient

from robot33 import config
from robot33.internal.model.user import USER_COLLECTION_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(config.get_settings().db.mongodb_url)
database = client.get_database(config.get_settings().db.mongodb_database)

user_collection = database.get_collection(USER_COLLECTION_NAME)
