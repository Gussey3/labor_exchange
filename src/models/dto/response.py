from pydantic import BaseModel


class ResponseUpdateDto(BaseModel):
    message: str


class ResponseCreateDto(ResponseUpdateDto):
    job_id: int
    user_id: int
