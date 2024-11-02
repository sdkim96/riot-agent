import uuid
from pydantic import BaseModel

class Skill(BaseModel):
    id: uuid.UUID
    name: str
    description: str

    is_ultimate: bool


class Skills(BaseModel):
    id: uuid.UUID
    q: Skill
    w: Skill
    e: Skill
    r: Skill