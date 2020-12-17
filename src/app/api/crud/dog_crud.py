from app.models.models import DogSchema
from app.db.db import user, dog, database
from app.api.crud import user_crud
import app.functions as fun





async def post(name: str, payload: DogSchema):
    """Post function to add a dog into the Database

    Args:
        name (str): Dogs name
        payload (DogSchema): dog information with pydantic structure    
                             
                            
    """    
    picture = fun.get_picture()
    query = dog.insert().values(
                                id=payload.id,
                                name=name,
                                picture=picture, 
                                is_adopted=False)
    await database.execute(query=query)


async def get(name: str):
    """ Search for the dog by name and return it    

    Args:
        name (str): [dog's name]

    Returns:
        ['databases.backends.postgres.Record']: [Record object with the 
                                                    information of the dog, none if the dog 
                                                    doesn't exits]
    """    
    query = dog.select().where(name == dog.c.name)
    return await database.fetch_one(query=query)

async def get_by_id(id: str):
    """ Search for the dog by id and return it    

    Args:
        id (str): [dog's id]

    Returns:
        ['databases.backends.postgres.Record']: [Record object with the 
                                                    information of the dog, none if the dog 
                                                    doesn't exits]
    """    
    query = dog.select().where(id == dog.c.id)
    return await database.fetch_one(query=query)

async def get_is_adopted():
    """ Search for the dog's that had the is_adopted column in True
        and returns all matches   

    Returns:
        ['databases.backends.postgres.Record']: [Record object with the 
                                                    information of the dogs, none if there aren't
                                                    adopted dogs]
    """    
    query = dog.select().where(dog.c.is_adopted == True)
    return await database.fetch_all(query=query)

async def get_all():
    """Returns all the dogs in the database

    Returns:
        ['databases.backends.postgres.Record']: [Record object with the 
                                                    information of the dogs, none if there are 
                                                    no dogs]
    """    
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
    await database.execute(query=query)


async def delete(name: str):
    query = dog.delete().where(name == dog.c.name)
    return await database.execute(query=query)


async def adopt_dog(payload):
        query = (
        dog
        .update()
        .where(payload.dog_name == dog.c.name)
        .values(id=dog.c.id ,name=dog.c.name, 
                is_adopted=True, picture=dog.c.picture, 
                created_date=dog.c.created_date, user_id=payload.user_id )
        .returning(dog.c.name)
    )
        return await database.execute(query=query)
