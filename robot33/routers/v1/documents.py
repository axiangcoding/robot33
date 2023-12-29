from datetime import datetime
import hashlib
from bson import ObjectId
from fastapi import APIRouter, Depends, Query
from robot33.dependencies.security import verify_token
from robot33.internal.model.document import DocumentInDb
from robot33.internal.schema.response import CommonResult
from pydantic import BaseModel, Field
from robot33.internal.db import database, document_dao

router = APIRouter(tags=["documents"], prefix="/documents", dependencies=[Depends(verify_token)])


class UploadDocumentIn(BaseModel):
    name: str = Field(description="文档名称")
    content: str = Field(description="文档内容")
    tag: str = Field(description="文档标签")


class UploadDocumentOut(BaseModel):
    document_id: str = Field(description="文档id")


@router.post("/upload", summary="上传文档")
def upload_document(body: UploadDocumentIn) -> CommonResult[UploadDocumentOut]:
    """上传文档

    上传文档

    :return:
    """
    # 计算字符串的md5
    content_md5 = hashlib.md5(body.content.encode("utf-8")).hexdigest()
    data = DocumentInDb(
        name=body.name,
        content=body.content,
        content_md5=content_md5,
        tag=body.tag,
        owner="",
    )
    id = document_dao.insert_one(data)
    return CommonResult.success(UploadDocumentOut(document_id=id))


class DocumentOut(BaseModel):
    name: str = Field(description="文档名称")
    content: str = Field(description="文档内容")
    tag: str = Field(description="文档标签")
    owner: str = Field(description="文档所有者")
    created_at: datetime = Field(description="创建时间")
    updated_at: datetime = Field(description="更新时间")


@router.get("/item", summary="获取文档")
def get_document(doc_id: str = Query(description="文档id")) -> CommonResult[DocumentOut]:
    """获取文档

    获取文档

    :return:
    """
    data = document_dao.find_one(doc_id)
    out = DocumentOut.model_validate(data.model_dump())
    return CommonResult.success(out)
