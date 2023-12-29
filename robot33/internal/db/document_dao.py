from bson import ObjectId
from robot33.internal.model.document import DocumentInDb
from robot33.internal.db.database import document_collection


def insert_one(data: DocumentInDb) -> str:
    item = document_collection.insert_one(data.model_dump())
    return str(item.inserted_id)


def delete_one(id: str) -> int:
    result = document_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count


def update_one(id: str, data: DocumentInDb) -> int:
    result = document_collection.update_one({"_id": ObjectId(id)}, {"$set": data.model_dump()})
    return result.modified_count

def find_one(id: str) -> DocumentInDb:
    result = document_collection.find_one({"_id": ObjectId(id)})
    return DocumentInDb.model_validate(result)


def find_all() -> list:
    result = document_collection.find()
    return [DocumentInDb.model_validate(item) for item in result]
