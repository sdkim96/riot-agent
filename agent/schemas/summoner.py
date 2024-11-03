from pydantic import BaseModel, Field


class Summoner(BaseModel):
    name: str = Field(description="Summoner name extracted from the query")
    tag: str = Field(description="Summoner tag extracted from the query")