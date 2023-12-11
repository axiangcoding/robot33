from enum import Enum


class LLMProviderType(str, Enum):
    BAIDU_ERNIE = "baidu_ernie"
    OPENAI_GPT = "openai_gpt"
