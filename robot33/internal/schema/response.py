from typing import Optional, TypeVar, Generic

from pydantic import BaseModel, Field

from robot33.internal.schema.errors import CommonError

# 定义一个类型变量
T = TypeVar("T")


class CommonResult(BaseModel, Generic[T]):
    code: int = Field(..., description="错误码")
    message: str = Field(..., description="错误信息")
    data: Optional[T] = Field(None, description="返回的数据")

    @classmethod
    def success(cls, data: Optional[T] = None):
        return cls(code=CommonError.SUCCESS.code, message="success", data=data)

    @classmethod
    def error(
        cls,
        ce: Optional[CommonError] = CommonError.ERROR,
        message: Optional[str] = None,
    ):
        return cls(code=ce.code, message=message if message else ce.description, data=None)
