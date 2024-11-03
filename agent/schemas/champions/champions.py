from typing import Optional
from pydantic import BaseModel

from .skills import Skills

class Champion(BaseModel):
    id: int
    name: str
    english_name: Optional[str] = None
    skills: Optional[Skills] = None
    