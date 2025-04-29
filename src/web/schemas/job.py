from typing import Optional

from pydantic import BaseModel, Field


class JobCreateSchema(BaseModel):
    """
    Схема создания объекта вакансия
    """
    title: Optional[str] = Field(description="Название вакансии")
    description: Optional[str] = Field(description="Описание вакансии")
    salary_from: Optional[str] = Field(description="Зарплата от")
    salary_to: Optional[str] = Field(description="Зарплата до")
    is_active: bool = Field(default=True, description="Флаг активности")


class JobSchema(JobCreateSchema):
    """
    Схема объекта вакансия
    """
    id: int = Field(description="Идентификатор вакансии")
    user_id: int = Field(description="Идентификатор пользователя")


class JobUpdateSchema(JobCreateSchema):
    """
    Схема обновления объекта вакансия
    """
    id: int = Field(description="Идентификатор вакансии")
