from typing import Optional

from pydantic import BaseModel


class ResponseCreateSchema(BaseModel):
    job_id: int
    message: Optional[str] = None


class ResponseSchema(BaseModel):
    id: int
    user_id: int
    job_id: int
    message: Optional[str] = None


class ResponseUpdateSchema(BaseModel):
    id: int
    message: Optional[str] = None
