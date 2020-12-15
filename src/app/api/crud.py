from app.models.models import DogSchema
from app.db.db import dog, database
import app.functions as fun

async def post(payload: DogSchema):
    picture = fun.get_picture()
    query = dog.insert().values(id=payload.id ,name=payload.name, picture=picture, is_adopted=payload.is_adopted)
    return await database.execute(query=query)

async def get(name: str):
    query = dog.select().where(name == dog.c.name)
    print(query)
    return await database.fetch_one(query=query)

async def get_all():
    query = dog.select()
    return await database.fetch_all(query=query)


async def put(name: str, payload: DogSchema):
    query = (
        dog
        .update()
        .where(name == dog.c.name)
        .values(id=payload.id ,name=payload.name, 
                is_adopted=payload.is_adopted, picture=dog.c.picture, 
                created_date=dog.c.created_date)
        .returning(dog.c.name)
    )
    print(query)
    return await database.execute(query=query)


async def delete(name: str):
    query = dog.delete().where(name == dog.c.name)
    return await database.execute(query=query)
