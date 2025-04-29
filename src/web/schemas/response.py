from typing import Optional

from pydantic import BaseModel, Field


class ResponseCreateSchema(BaseModel):
    """
    Схема создания объекта отклик
    """
    job_id: int = Field(description="Идентификатор вакансии")
    message: Optional[str] = Field(description="Сопроводительное письмо")


class ResponseSchema(BaseModel):
    """
    Схема объекта отклик
    """
    id: int = Field(description="Идентификатор отклика")
    user_id: int = Field(description="Идентификатор пользователя")
    job_id: int = Field(description="Идентификатор вакансии")
    message: Optional[str] = Field(description="Сопроводительное письмо")


class ResponseUpdateSchema(BaseModel):
    """
    Схема обновления объекта отклик
    """
    id: int = Field(description="Идентификатор отклика")
    message: Optional[str] = Field(description="Сопроводительное письмо")
