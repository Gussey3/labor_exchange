from pydantic import BaseModel, Field


class ResponseUpdateDto(BaseModel):
    """
    Модель данных для обновления откликов
    """

    message: str = Field(description="Сопроводительное письмо")


class ResponseCreateDto(BaseModel):
    """
    Модель данных для создания откликов
    """

    job_id: int = Field(description="Идентификатор вакансии")
    user_id: int = Field(description="Идентификатор пользователя")
    message: str = Field(description="Сопроводительное письмо")
