import pytest
from fastapi.testclient import TestClient

default_headers = {"X-Robot33-Token": "default_token"}


def test_llm_chat_fake(test_client: TestClient):
    response = test_client.post(
        "/v1/ai/llm/chat",
        json={
            "llm_provider": "fake",
            "messages": [
                {
                    "role": "user",
                    "content": "你好",
                }
            ],
        },
        headers=default_headers,
    )
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert resp_json["data"]["result"] == "i am fake response"


@pytest.mark.skip("需要配置百度API的key")
def test_llm_chat_baidu_ernie(test_client: TestClient):
    response = test_client.post(
        "/v1/ai/llm/chat",
        json={
            "llm_provider": "baidu_ernie",
            "messages": [
                {
                    "role": "user",
                    "content": "你好",
                }
            ],
        },
        headers=default_headers,
    )
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert "result" in resp_json["data"]["result"]
