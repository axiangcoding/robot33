from httpx import AsyncClient

from robot33.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

async_client = AsyncClient(app=app, base_url="http://localhost:8888")
