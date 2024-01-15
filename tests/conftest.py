import pytest
from loguru import logger
from starlette.testclient import TestClient

from robot33.internal.db import database
from robot33.main import app


@pytest.fixture(scope="module")
def test_client():
    yield TestClient(app)


@pytest.fixture(scope="module")
def test_token_header() -> dict[str, str]:
    return {"X-Robot33-Token": "default_token"}


@pytest.fixture(scope="function")
def test_document_collection():
    logger.info("setup document_collection")
    database.document_collection.drop()
    yield database.document_collection
    logger.info("teardown document collection")
    database.document_collection.drop()
