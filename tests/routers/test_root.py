from tests.test_main import client


def test_get_health():
    with client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"code": 0, "data": {"status": "ok"}, "message": "success"}
