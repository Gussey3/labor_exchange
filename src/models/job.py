from dataclasses import dataclass, field

from models.response import Response


@dataclass
class Job:
    id: int
    user_id: int
    title: str
    description: str
    salary_from: str
    salary_to: str
    is_active: bool

    responses: list[Response] = field(default_factory=list)
