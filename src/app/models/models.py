from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DogSchema(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    is_adopted: bool


class DogDB(DogSchema):
    id: str
    picture: Optional[str]
    created_date: Optional[datetime]
   
