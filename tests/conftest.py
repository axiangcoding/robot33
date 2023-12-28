import pytest
from starlette.testclient import TestClient

from robot33.main import app


@pytest.fixture(scope="module")
def test_client():
    yield TestClient(app)
