from robot33.internal.model.base import BaseDBSchema

DOCUMENT_COLLECTION_NAME = "document"


class DocumentInDb(BaseDBSchema):
    name: str
    content: str
    content_md5: str
    tag: str
    owner: str
