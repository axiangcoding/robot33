from starlette.testclient import TestClient


def test_get_health(test_client: TestClient):
    with test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        resp = response.json()
        assert resp["code"] == 0
        assert resp["message"] == "success"
        assert resp["data"]["app_status"] == "ok"
        # assert resp["data"]["db_status"] == "ok"
