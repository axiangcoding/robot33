from typing import Optional

from langchain_community.chat_models import FakeListChatModel

from robot33 import config
from robot33.internal.schema.common import LLMProviderType
from langchain.chat_models import QianfanChatEndpoint, ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel


def get_chat_model_client(
    provider: LLMProviderType, model: Optional[str] = None, streaming: Optional[bool] = False
) -> BaseChatModel:
    """
    获取LLM客户端

    :param provider: 服务提供商
    :param model: 模型名称
    :param streaming: 是否流式
    :return: langchain的llm客户端
    """
    if provider == LLMProviderType.BAIDU_ERNIE:
        if model is None:
            model = "ERNIE-Bot-turbo"
        llm = QianfanChatEndpoint(
            **config.get_settings().llm_config.baidu_ernie,
            model=model,
            streaming=streaming,
        )
    elif provider == LLMProviderType.OPENAI_GPT:
        if model is None:
            model = "gpt-3.5-turbo"
        llm = ChatOpenAI(
            **config.get_settings().llm_config.openai_gpt,
            model=model,
            streaming=streaming,
        )
    elif provider == LLMProviderType.FAKE:
        llm = FakeListChatModel(**config.get_settings().llm_config.fake)
    else:
        raise NotImplementedError("this provider is not implemented")
    return llm
