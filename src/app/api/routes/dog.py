from typing import List

import app.functions as fun
from app.api.crud import dog_crud, user_crud
from app.models.models import DogSchema, DogDB, AdoptSchema
from fastapi import APIRouter, HTTPException, Path, Query

router = APIRouter()


@router.post("/{name}", status_code=201)
async def create_dog(payload: DogSchema, name: str = Path(...)):
    dog_exist_id = await dog_crud.get_by_id(payload.id)
    dog_exist_name = await dog_crud.get(name)
    if dog_exist_id:
        raise HTTPException(status_code=409, detail="id already exists")
    if dog_exist_name:
        raise HTTPException(status_code=409, detail="name already exists")
    await dog_crud.post(name, payload)
    new_dog = await dog_crud.get(name)
    return new_dog



@router.get("/", response_model=List[DogDB])
async def read_all_dogs():
    return await dog_crud.get_all()

@router.get("/{name}/", response_model=DogDB)
async def read_dog(name: str = Path(..., min_length=1),):
    dog = await dog_crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog

@router.get("/is_adopted", response_model=DogDB)
async def read_dog():
    dog = await dog_crud.get_is_adopted()
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog

@router.put("/{name}/", response_model=DogSchema)
async def update_dog(payload: DogSchema, name: str = Path(..., min_length=1),):
    dog = await dog_crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    dog_id = await dog_crud.put(name, payload)

    return dog


@router.delete("/{name}/", response_model=DogDB)
async def delete_dog(name: str = Path(..., min_length=1)):
    dog = await dog_crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    await dog_crud.delete(name)

    return dog

@router.put("/adopt/{dog_name}", response_model=DogDB)
async def update_dog(payload: AdoptSchema):
    dog = await dog_crud.get(payload.dog_name)
    user_exist_id = await user_crud.get_by_id(payload.user_id)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")
    elif not user_exist_id:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        dog_id = await dog_crud.adopt_dog(payload)
    new_dog = await dog_crud.get(payload.dog_name)
    return new_dog