from abc import ABC, abstractmethod
from pydantic import BaseModel
from pymongo import MongoClient

from robot33 import config
from robot33.internal.model.document import DOCUMENT_COLLECTION_NAME

client = MongoClient(config.get_settings().db.mongodb_url)
database = client.get_database(config.get_settings().db.mongodb_database)

document_collection = database.get_collection(DOCUMENT_COLLECTION_NAME)


class DBDAO(ABC, BaseModel):
    @abstractmethod
    def insert_one(self, data: BaseModel) -> str:
        pass

    @abstractmethod
    def delete_one(self, id: str) -> int:
        pass

    @abstractmethod
    def update_one(self, id: str, data: BaseModel) -> int:
        pass

    @abstractmethod
    def find_one(self, id: str) -> BaseModel:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass
