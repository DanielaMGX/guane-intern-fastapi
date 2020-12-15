from app.api.models import DogSchema
from app.db.db import dog, database


async def post(payload: DogSchema):
    query = dog.insert().values(id=payload.id ,name=payload.name, 
                                picture=payload.picture, is_adopted=payload.is_adopted)
    return await database.execute(query=query)


async def get(id: str):
    query = dog.select().where(id == dog.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = dog.select()
    return await database.fetch_all(query=query)


async def put(id: str, payload: DogSchema):
    query = (
        dog
        .update()
        .where(id == dog.c.id)
        .values(id=payload.id ,name=payload.name, 
                                picture=payload.picture, is_adopted=payload.is_adopted)
        .returning(dog.c.id)
    )
    return await database.execute(query=query)


async def delete(id: str):
    query = dog.delete().where(id == dog.c.id)
    return await database.execute(query=query)
