from dataclasses import dataclass


@dataclass
class Response:
    """
    Модель отклика на вакансию
    """

    id: int
    job_id: int
    user_id: int
    message: str
