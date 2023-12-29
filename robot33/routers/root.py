from fastapi import APIRouter
from pydantic import BaseModel, Field
from robot33.internal.schema.response import CommonResult

router = APIRouter(tags=["root"], prefix="")


class HealthOut(BaseModel):
    app_status: str = Field("ok", description="应用状态")
    # db_status: str = Field("ok", description="数据库状态")


@router.get("/health", summary="获取应用的健康状态")
async def get_health() -> CommonResult[HealthOut]:
    """获取应用的健康状态

    获取应用的健康状态，如果返回的状态码为200，则表示应用正常运行

    :return:
    """
    out = HealthOut()
    # stat = db.database.command("ping")
    # if stat["ok"] != 1:
    #     out.db_status = "ping error"
    return CommonResult.success(out)
