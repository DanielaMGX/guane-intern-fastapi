from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DogSchema(BaseModel):
    id: str
    is_adopted: bool


class DogDB(DogSchema):
    #id: str
    name: str 
    picture: Optional[str]
    created_date: Optional[datetime]
    
   
