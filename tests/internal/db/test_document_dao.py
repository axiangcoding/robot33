from bson import ObjectId
from robot33.internal.db.document_dao import DocumentDAO
from robot33.internal.model.document import DocumentInDb


def test_insert_one(
    test_document_collection,
):
    id = DocumentDAO(test_document_collection).insert_one(
        DocumentInDb(name="test", 
                     content="test", 
                     content_md5="test",
                     tag="test", 
                     owner="test")
    )

    found = test_document_collection.find_one({"_id": ObjectId(id)})

    assert found is not None
    assert found["name"] == "test"
    assert found["content"] == "test"
    assert found["content_md5"] == "test"
    assert found["tag"] == "test"
    assert found["owner"] == "test"

def test_delete_one(
    test_document_collection,
):
    res = test_document_collection.insert_one(
        DocumentInDb(name="test", 
                     content="test", 
                     content_md5="test",
                     tag="test", 
                     owner="test").model_dump()
    )

    DocumentDAO(test_document_collection).delete_one(res.inserted_id)

    found = test_document_collection.find_one({"_id": ObjectId(res.inserted_id)})

    assert found is None

