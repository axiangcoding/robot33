from robot33.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
