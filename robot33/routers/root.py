from fastapi import APIRouter

from robot33.internal.schema.response import CommonResult

router = APIRouter(tags=["root"], prefix="")


@router.get("/health", summary="获取应用的健康状态")
async def get_health() -> CommonResult:
    """获取应用的健康状态

    获取应用的健康状态，如果返回的状态码为200，则表示应用正常运行

    :return:
    """
    return CommonResult.success({"status": "ok"})
