from typing import Optional

from robot33 import config
from robot33.internal.schema.common import LLMProviderType
from langchain.llms import QianfanLLMEndpoint, OpenAI
from langchain.llms.base import LLM


def get_llm_client(provider: LLMProviderType, model: Optional[str] = None, streaming: Optional[bool] = False) -> LLM:
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
        llm = QianfanLLMEndpoint(
            **config.get_settings().llm_config.baidu_ernie,
            model=model,
            streaming=streaming,
        )
        return llm
    elif provider == LLMProviderType.OPENAI_GPT:
        if model is None:
            model = "gpt-3.5-turbo"
        llm = OpenAI(
            **config.get_settings().llm_config.openai_gpt,
            model=model,
            streaming=streaming,
        )
        return llm
    else:
        raise NotImplementedError("暂不支持该LLM服务提供商")
