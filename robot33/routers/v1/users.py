from fastapi import APIRouter
from robot33.internal.db import database
from robot33.internal.schema.response import CommonResult

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/me", summary="获取当前用户的信息")
async def get_me() -> CommonResult:
    users = []
    async for user in database.user_collection.find():
        users.append(user)
    """获取当前用户的信息

    获取当前用户的信息，包括用户的ID、用户名、邮箱等

    :return: 当前用户的信息
    """
    return CommonResult.success(users)


@router.post("/token", summary="用户登录，并获取token")
async def login() -> CommonResult:
    """用户登录，并获取token

    用户登录，并获取token

    :return: 当前用户的信息
    """
    return CommonResult.success()
