from pydantic import BaseModel


class ContentSSMLRequest(BaseModel):
    content: str


class ContentSSMLResponse(BaseModel):
    code: int
    status: str
    message: str
    ssml: str
