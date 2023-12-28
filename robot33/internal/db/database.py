from pymongo import MongoClient

from robot33 import config
from robot33.internal.model.document import DOCUMENT_COLLECTION_NAME

client = MongoClient(config.get_settings().db.mongodb_url)
database = client.get_database(config.get_settings().db.mongodb_database)

document_collection = database.get_collection(DOCUMENT_COLLECTION_NAME)
