import uuid
from pydantic import BaseModel

class Skill(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str = None
    description: str = None


class Skills(BaseModel):
    """
    cass.Champion.passive.name
    cass.Champion.passive.description
    cass.Champion.spells[0].name
    cass.Champion.spells[0].description
    """
    id: uuid.UUID = uuid.uuid4()
    passive: Skill = None
    q: Skill = None
    w: Skill = None
    e: Skill = None
    r: Skill = None