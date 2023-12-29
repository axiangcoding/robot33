import pytest
from fastapi.testclient import TestClient

from robot33 import config


__chat_path__ = "/v1/ai/chat"


def test_llm_chat_fake(test_client: TestClient, test_token_header: dict[str, str]):
    response = test_client.post(
        __chat_path__,
        json={
            "llm_provider": "fake",
            "messages": [
                {
                    "role": "user",
                    "content": "你好",
                }
            ],
        },
        headers=test_token_header,
    )
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert resp_json["data"]["result"] == "i am fake response"


@pytest.mark.skipif(config.get_settings().llm_config.baidu_ernie is None, reason="需要配置百度文心一言的key和secret")
def test_llm_chat_baidu_ernie(test_client: TestClient, test_token_header: dict[str, str]):
    response = test_client.post(
        __chat_path__,
        json={
            "llm_provider": "baidu_ernie",
            "messages": [
                {
                    "role": "user",
                    "content": "你好",
                }
            ],
        },
        headers=test_token_header,
    )
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert "result" in resp_json["data"]


@pytest.mark.skipif(config.get_settings().llm_config.openai_gpt is None, reason="需要配置Openai的key")
def test_llm_chat_openai_gpt(test_client: TestClient, test_token_header: dict[str, str]):
    response = test_client.post(
        __chat_path__,
        json={
            "llm_provider": "openai_gpt",
            "messages": [
                {
                    "role": "user",
                    "content": "你好",
                }
            ],
        },
        headers=test_token_header,
    )
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert "result" in resp_json["data"]


@pytest.mark.skipif(config.get_settings().llm_config.baidu_ernie is None, reason="需要配置百度文心一言的key和secret")
def test_llm_chat_baidu_ernie_function_call(test_client: TestClient, test_token_header: dict[str, str]):
    response = test_client.post(
        __chat_path__,
        json={
            "llm_provider": "baidu_ernie",
            "llm_model": "ERNIE-Bot",
            "messages": [
                {
                    "role": "user",
                    "content": "北京的天气如何？",
                }
            ],
            "functions": [
                {
                    "name": "get_weather",
                    "description": "get weather of a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "location name",
                            },
                        },
                        "required": ["location"],
                    },
                },
            ],
        },
        headers=test_token_header,
    )
    assert response.status_code == 200
    resp_json = response.json()
    print(resp_json)
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert resp_json["data"]["result"] == ""
    assert resp_json["data"]["additional_info"]["function_call"]["name"] == "get_weather"
    assert resp_json["data"]["additional_info"]["finish_reason"] == "function_call"


@pytest.mark.skipif(config.get_settings().llm_config.openai_gpt is None, reason="需要配置Openai的key")
def test_llm_chat_openai_gpt_function_call(test_client: TestClient, test_token_header: dict[str, str]):
    response = test_client.post(
        __chat_path__,
        json={
            "llm_provider": "openai_gpt",
            "llm_model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "北京的天气如何？",
                }
            ],
            "functions": [
                {
                    "name": "get_weather",
                    "description": "get weather of a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "location name",
                            },
                        },
                        "required": ["location"],
                    },
                },
            ],
        },
        headers=test_token_header,
    )
    assert response.status_code == 200
    resp_json = response.json()
    print(resp_json)
    assert resp_json["code"] == 0
    assert resp_json["message"] == "success"
    assert resp_json["data"]["result"] == ""
    assert resp_json["data"]["additional_info"]["function_call"]["name"] == "get_weather"
