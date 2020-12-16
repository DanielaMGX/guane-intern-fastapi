from app.models.models import UserSchema
from app.db.db import user, user, database

async def post(payload: UserSchema):
    query = user.insert().values(
                                id=payload.id,
                                first_name=payload.first_name,
                                last_name=payload.last_name,
                                email=payload.email)
    return await database.execute(query=query)

async def get_by_id(id: int):
    query = user.select().where(id == user.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = user.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: UserSchema):
    query = (
        user
        .update()
        .where(id == user.c.id)
        .values(id=id,
                first_name=payload.first_name,
                last_name=payload.last_name,
                email=payload.email,
                created_date=user.c.created_date)
        .returning(user.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = user.delete().where(id == user.c.id)
    return await database.execute(query=query)