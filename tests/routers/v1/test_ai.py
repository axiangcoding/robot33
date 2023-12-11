from tests.test_main import client


def test_llm_chat():
    with client:
        response = client.post(
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
        )
        assert response.status_code == 200

        assert response.json()["code"] == 0
        assert response.json()["message"] == "success"
        assert "result" in response.json()["data"]
