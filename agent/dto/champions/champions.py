from pydantic import BaseModel

from .skills import Skill

class Champion(BaseModel):
    id: int
    name: str
    skills: Skill
    