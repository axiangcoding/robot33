from typing import Optional

from pydantic import BaseModel

USER_COLLECTION_NAME = "user"


class UserInDb(BaseModel):
    username: str
    password: str
    nickname: Optional[str]
