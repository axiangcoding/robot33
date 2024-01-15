from datetime import datetime, timezone

from pydantic import BaseModel, Field


class BaseDBSchema(BaseModel):
    created_at: datetime = Field(default=datetime.now(timezone.utc), description="创建时间")
    updated_at: datetime = Field(default=datetime.now(timezone.utc), description="更新时间")
