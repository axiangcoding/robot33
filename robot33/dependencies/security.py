import secrets
from typing import Optional

from fastapi import HTTPException
from fastapi.security import APIKeyHeader
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from robot33 import config


class VerifyTokenHeader(APIKeyHeader):
    async def __call__(self, request: Request) -> Optional[str]:
        api_key = await super().__call__(request)
        if secrets.compare_digest(api_key, config.get_settings().security.token):
            return None
        else:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Authenticated Failed")


verify_token = VerifyTokenHeader(name="X-Robot33-Token", scheme_name="Auth Token", description="token for api usage")
