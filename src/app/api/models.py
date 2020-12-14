from pydantic import BaseModel


class DogSchema(BaseModel):
    id: str
    name: str
    picture: str
    is_adopted: bool

class DogDB(DogSchema):
    id: str