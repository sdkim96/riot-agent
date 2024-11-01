from pydantic import BaseModel, Field

class Intent(BaseModel):
    rank_1_code: int = Field(description="most possible intent code value")
    rank_1_description: str = Field(description="most possible description of that intent")
    rank_2_code: int = Field(description="second possible intent code value")
    rank_2_description: str = Field(description="second possible description of that intent")


class Summoner(BaseModel):
    name: str = Field(description="Summoner name extracted from the query")
    tag: str = Field(description="Summoner tag extracted from the query")