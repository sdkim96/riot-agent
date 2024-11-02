from typing import Optional
from pydantic import BaseModel, Field

class Intent(BaseModel):
    rank_1_code: int = Field(description="Most probable intent code derived from the given information")
    rank_1_description: str = Field(description="Description of the most probable intent")
    rank_2_code: Optional[int] = Field(None, description="Second probable intent code derived from the given information")
    rank_2_description: Optional[str] = Field(None, description="Description of the second probable intent")
    rank_3_code: Optional[int] = Field(None, description="Third probable intent code derived from the given information")
    rank_3_description: Optional[str] = Field(None, description="Description of the third probable intent")

class Summoner(BaseModel):
    name: str = Field(description="Summoner name extracted from the query")
    tag: str = Field(description="Summoner tag extracted from the query")