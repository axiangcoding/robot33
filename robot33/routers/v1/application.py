from fastapi import APIRouter

from robot33 import config
from robot33.internal.schema.response import CommonResult
from pydantic import BaseModel

router = APIRouter(tags=["application"], prefix="/application")


class InfoOut(BaseModel):
    version: str


@router.get("/info", summary="获取应用的信息")
async def get_info() -> CommonResult[InfoOut]:
    """获取应用的信息

    获取应用的信息，包括名称、版本、描述等

    :return: 应用的信息
    """
    return CommonResult[InfoOut].success(InfoOut(version=config.get_settings().app.version))


@router.get("/health", summary="获取应用的健康状态")
async def get_health() -> CommonResult:
    """获取应用的健康状态

    获取应用的健康状态，如果返回的状态码为200，则表示应用正常运行

    :return:
    """
    return CommonResult.success({"status": "ok"})
