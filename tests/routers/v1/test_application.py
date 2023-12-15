from tests.test_main import client


def test_get_info():
    with client:
        response = client.get("/v1/application/info")
        assert response.status_code == 200
        assert response.json() == {"code": 0, "data": {"version": "development"}, "message": "success"}
