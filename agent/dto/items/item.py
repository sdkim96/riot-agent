import uuid

from pydantic import BaseModel

class Item(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    price: int