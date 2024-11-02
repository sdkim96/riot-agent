from typing import Optional
from pydantic import BaseModel, Field

class Intent(BaseModel):
    rank_1_code: int = Field(description="Most probable intent code derived from the given information")
    rank_2_code: Optional[int] = Field(None, description="Second probable intent code derived from the given information")
    rank_3_code: Optional[int] = Field(None, description="Third probable intent code derived from the given information")
