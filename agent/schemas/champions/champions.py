from typing import Optional
from pydantic import BaseModel

from .skills import Skills

class Champion(BaseModel):
    id: int
    name: str
    skills: Optional[Skills] = None
    