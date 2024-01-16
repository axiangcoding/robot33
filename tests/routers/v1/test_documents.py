import hashlib

import pytest
from bson import ObjectId
from fastapi.testclient import TestClient

from robot33.internal.model.document import DocumentInDb


@pytest.mark.parametrize(
    "name,content,tag",
    [
        ("test_document_1", "test_content_1", "test_tag_1"),
        ("test_document_2", "test_content_2", "test_tag_2"),
        ("test_document_3", "test_content_3", "test_tag_3"),
    ],
)
def test_upload_document(
    test_client: TestClient,
    test_token_header: dict[str, str],
    test_document_collection,
    name: str,
    content: str,
    tag: str,
):
    with test_client:
        response = test_client.post(
            "/v1/documents/upload",
            json={
                "name": name,
                "content": content,
                "tag": tag,
            },
            headers=test_token_header,
        )

    assert response.status_code == 200
    resp = response.json()
    assert resp["code"] == 0

    assert "document_id" in resp["data"]

    document_id = resp["data"]["document_id"]
    item = test_document_collection.find_one({"_id": ObjectId(document_id)})

    assert document_id == str(item["_id"])
    assert name == item["name"]
    assert content == item["content"]
    assert tag == item["tag"]
    assert hashlib.md5(content.encode("utf-8")).hexdigest() == item["content_md5"]


@pytest.mark.parametrize(
    "name,content,tag",
    [
        ("test_document_1", "test_content_1", "test_tag_1"),
        ("test_document_2", "test_content_2", "test_tag_2"),
        ("test_document_3", "test_content_3", "test_tag_3"),
    ],
)
def test_get_document(
    test_client: TestClient,
    test_token_header: dict[str, str],
    test_document_collection,
    name: str,
    content: str,
    tag: str,
):
    data = DocumentInDb(
        name=name,
        content=content,
        content_md5=hashlib.md5(content.encode("utf-8")).hexdigest(),
        tag=tag,
        owner="",
    )
    inserted = test_document_collection.insert_one(data.model_dump())
    id = str(inserted.inserted_id)
    with test_client:
        response = test_client.get(
            "/v1/documents/item",
            params={
                "doc_id": id,
            },
            headers=test_token_header,
        )
    assert response.status_code == 200
    resp = response.json()
    assert resp["code"] == 0
    assert resp["data"]["name"] == name
    assert resp["data"]["content"] == content
    assert resp["data"]["tag"] == tag
    assert resp["data"]["owner"] == ""
    assert resp["data"]["created_at"] is not None
    assert resp["data"]["updated_at"] is not None
