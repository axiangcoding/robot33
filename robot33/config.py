from functools import lru_cache
from os import path
from typing import Any, Dict, Optional, Tuple

import tomllib
from loguru import logger
from pydantic.fields import FieldInfo
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)


class App(BaseSettings):
    name: str = "Robot33 API"
    version: str = "development"
    description: str = ""
    debug: bool = False


class LLMConfig(BaseSettings):
    baidu_ernie: Optional[dict[str, Any]] = None
    openai_gpt: Optional[dict[str, Any]] = None
    fake: Optional[dict[str, Any]] = None


class Security(BaseSettings):
    token: str = "default_token"


class Database(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_database: str = "robot33"


class Settings(BaseSettings):
    app: App = App()
    llm_config: LLMConfig = LLMConfig()
    security: Security
    db: Database

    model_config = SettingsConfigDict(env_nested_delimiter="__")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            TomlConfigSettingsSource(settings_cls, config_file_path="./local.app.toml"),
            TomlConfigSettingsSource(settings_cls, config_file_path=None),
            dotenv_settings,
            file_secret_settings,
        )


class TomlConfigSettingsSource(PydanticBaseSettingsSource):
    config_file_path: Optional[str] = "./app.toml"

    def __init__(self, settings_cls: type[BaseSettings], config_file_path: Optional[str]):
        super().__init__(settings_cls)
        if config_file_path is not None:
            self.config_file_path = config_file_path

    def get_field_value(self, field: FieldInfo, field_name: str) -> Tuple[Any, str, bool]:
        file_content_toml = get_dict_from_toml_file(self.config_file_path)
        if not file_content_toml:
            logger.debug(
                "Not found config field {} in config file {}",
                field_name,
                self.config_file_path,
            )
            return None, field_name, False
        logger.debug("Found config field {} in config file {}", field_name, self.config_file_path)
        field_value = file_content_toml.get(field_name)
        return field_value, field_name, False

    def prepare_field_value(self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool) -> Any:
        return value

    def __call__(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(field, field_name)
            field_value = self.prepare_field_value(field_name, field, field_value, value_is_complex)
            if field_value is not None:
                d[field_key] = field_value

        return d


@lru_cache
def get_dict_from_toml_file(file_path: str) -> dict:
    if not path.exists(file_path):
        logger.debug("toml file {} not exist", file_path)
        return {}
    with open(file_path, "rb") as f:
        file_content_toml = tomllib.load(f)
    logger.debug("toml file {} exist", file_path)
    return file_content_toml


@lru_cache
def get_settings() -> Settings:
    logger.info("Loading config settings from the environment and toml file...")
    return Settings()
