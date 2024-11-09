from pydantic import BaseModel

class Map(BaseModel):
    id: int = None
    name: str = None
    english_name: str = None