from asyncio import get_event_loop
from typing import Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from starlette.testclient import TestClient

from robot33.main import app


# FIXME 这里的async_client可能会无法正常工作，需要验证
@pytest_asyncio.fixture(scope="module")
async def async_client() -> Generator:
    yield AsyncClient(app=app, base_url="http://testserver")


@pytest.fixture(scope="module")
def test_client():
    yield TestClient(app)
