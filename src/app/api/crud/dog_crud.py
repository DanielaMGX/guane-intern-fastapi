from app.models.models import DogSchema
from app.db.db import user, dog, database
import app.functions as fun

async def post(name: str, payload: DogSchema):
    picture = fun.get_picture()
    query = dog.insert().values(
                                id=payload.id,
                                name=name,
                                picture=picture, 
                                is_adopted=payload.is_adopted)
    return await database.execute(query=query)

async def get(name: str):
    query = dog.select().where(name == dog.c.name)
    return await database.fetch_one(query=query)

async def get_by_id(id: str):
    query = dog.select().where(id == dog.c.id)
    return await database.fetch_one(query=query)

async def get_is_adopted():
    query = dog.select().where(True == dog.c.is_adopted)
    return await database.fetch_one(query=query)

async def get_all():
    query = dog.select()
    return await database.fetch_all(query=query)


async def put(name: str, payload: DogSchema):
    query = (
        dog
        .update()
        .where(name == dog.c.name)
        .values(id=payload.id ,name=name, 
                is_adopted=payload.is_adopted, picture=dog.c.picture, 
                created_date=dog.c.created_date)
        .returning(dog.c.name)
    )
    print(query)
    return await database.execute(query=query)


async def delete(name: str):
    query = dog.delete().where(name == dog.c.name)
    return await database.execute(query=query)

