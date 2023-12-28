from fastapi import Request
from fastapi.responses import JSONResponse

from robot33.internal.schema.errors import CommonError
from robot33.internal.schema.response import CommonResult


async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=CommonResult.error(
            ce=CommonError.ERROR,
            message=f"{type(exc)} - {str(exc)}",
        ).model_dump(),
    )
