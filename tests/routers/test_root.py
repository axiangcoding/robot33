from starlette.testclient import TestClient


def test_get_health(test_client: TestClient):
    with test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"code": 0, "data": {"status": "ok"}, "message": "success"}
