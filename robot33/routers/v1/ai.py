from typing import Optional

from fastapi import APIRouter, Depends
from langchain_community.callbacks import get_openai_callback
from langchain_core.messages import (
    FunctionMessage,
    AIMessage,
    SystemMessage,
    HumanMessage,
)
from langchain_core.messages.base import BaseMessage
from pydantic import BaseModel, Field

from robot33.internal.schema.common import LLMProviderType
from robot33.internal.schema.response import CommonResult
from robot33.internal.service import ai
from loguru import logger
from robot33.dependencies.security import verify_token

router = APIRouter(tags=["ai"], prefix="/ai", dependencies=[Depends(verify_token)])


class ChatMessage(BaseModel):
    role: str = Field(
        description="消息角色，可以是assistant或者user，部分模型支持system和function",
        pattern="^(assistant|user|system|function)$",
    )
    content: str = Field(description="消息内容")
    name: Optional[str] = Field(
        description="如果是function的消息，则需要指定function的名称", default=None
    )


class LLMChatIn(BaseModel):
    llm_provider: LLMProviderType = Field(description="LLM服务提供商")
    llm_model: Optional[str] = Field(
        description="LLM模型名称，如果不指定则随机选择", default=None
    )
    messages: list[ChatMessage]
    functions: list[dict] = Field(
        description="函数定义列表。如果模型支持function calling，则可以指定来使用，否则无效。",
        default=None,
    )


class LLMChatOut(BaseModel):
    result: str = Field(description="AI的响应")
    additional_info: Optional[dict] = Field(description="额外的信息", default=None)


@router.post("/chat", summary="和大语言模型聊天")
def llm_chat(body: LLMChatIn) -> CommonResult[LLMChatOut]:
    """和大语言模型聊天

    :param body:
    :return:
    """
    chat_model = ai.get_chat_model_client(body.llm_provider, body.llm_model)

    msgs = convert_to_langchain_messages(body.messages)
    with get_openai_callback() as cb:
        resp = chat_model.invoke(msgs, functions=body.functions)
    logger.debug("token usage callback is {}", cb)
    return CommonResult.success(
        LLMChatOut(result=resp.content, additional_info=resp.additional_kwargs)
    )


def convert_to_langchain_messages(messages: list[ChatMessage]) -> list[BaseMessage]:
    """
    将请求的消息转换为LangChain的消息
    :param messages:
    :return:
    """
    msgs = []
    for msg in messages:
        if msg.role == "function":
            m = FunctionMessage(content=msg.content, name=msg.name)
        elif msg.role == "system":
            m = SystemMessage(content=msg.content)
        elif msg.role == "ai":
            m = AIMessage(content=msg.content)
        elif msg.role == "user":
            m = HumanMessage(content=msg.content)
        else:
            raise ValueError("不支持的消息角色")
        msgs.append(m)
    return msgs
