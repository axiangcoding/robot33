from starlette.testclient import TestClient


def test_get_info(test_client: TestClient):
    with test_client:
        response = test_client.get("/v1/application/info")
    assert response.status_code == 200
    assert response.json() == {"code": 0, "data": {"version": "development"}, "message": "success"}
