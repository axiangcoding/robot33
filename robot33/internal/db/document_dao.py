from datetime import datetime, timezone
from bson import ObjectId
from robot33.internal.model.document import DocumentInDb
from robot33.internal.db.database import DBDAO, document_collection
from pymongo.collection import Collection


class DocumentDAO(DBDAO):
    __col__: Collection = document_collection

    def __init__(self, collection: Collection = None):
        if collection is not None:
            self.__col__ = collection

    def insert_one(self, data: DocumentInDb) -> str:
        item = self.__col__.insert_one(data.model_dump())
        return str(item.inserted_id)

    def delete_one(self, id: str) -> int:
        result = self.__col__.delete_one({"_id": ObjectId(id)})
        return result.deleted_count

    def update_one(self, id: str, data: DocumentInDb) -> int:
        data.updated_at = datetime.now(timezone.utc)
        result = self.__col__.update_one(
            {"_id": ObjectId(id)}, {"$set": data.model_dump(exclude_unset=True)}
        )
        return result.modified_count

    def find_one(self, id: str) -> DocumentInDb:
        result = self.__col__.find_one({"_id": ObjectId(id)})
        return DocumentInDb.model_validate(result)

    def find_all(self) -> list:
        result = self.__col__.find()
        return [DocumentInDb.model_validate(item) for item in result]
