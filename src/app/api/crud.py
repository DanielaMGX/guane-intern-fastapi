from app.api.models import DogSchema
from app.db.db import dog, database


async def post(payload: DogSchema):
    query = dog.insert().values(id=payload.id ,name=payload.name, 
                                picture=payload.picture, is_adopted=payload.is_adopted)
    return await database.execute(query=query)
