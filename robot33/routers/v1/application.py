from fastapi import APIRouter
from pydantic import BaseModel

from robot33 import config
from robot33.internal.schema.response import CommonResult

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
