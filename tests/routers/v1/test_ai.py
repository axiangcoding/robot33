import pytest

from tests.test_main import async_client

default_headers = {"X-Robot33-Token": "default_token"}


@pytest.mark.asyncio
async def test_llm_chat_fake():
    async with async_client as ac:
        response = await ac.post(
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
