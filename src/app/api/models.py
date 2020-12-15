from pydantic import BaseModel, Field


class DogSchema(BaseModel):
    id: str = Field(..., min_length=1)
    name: str
    picture: str
    is_adopted: bool

class DogDB(DogSchema):
    id: str