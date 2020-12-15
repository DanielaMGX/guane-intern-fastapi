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
    
class UserSchema(BaseModel):
    id: int = Field(..., gt=0)
    first_name: str
    last_name: str
    email: str

class UserDB(UserSchema):
    created_date: datetime
