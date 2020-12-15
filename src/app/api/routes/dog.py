from typing import List

import app.functions as fun
from app.api import crud
from app.models.models import DogSchema, DogDB
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/",response_model=DogDB, status_code=201)
async def create_dog(payload: DogSchema):
    dog_id = await crud.post(payload)
    response_object = {
        "id": payload.id,
        "name": payload.name,
        "is_adopted": payload.is_adopted,

    }
    return response_object



@router.get("/", response_model=List[DogDB])
async def read_all_dogs():
    return await crud.get_all()

@router.get("/{name}/", response_model=DogDB)
async def read_dog(name: str = Path(..., min_length=1),):
    dog = await crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog


@router.put("/{name}/", response_model=DogSchema)
async def update_dog(payload: DogSchema, name: str = Path(..., min_length=1),):
    dog = await crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    dog_id = await crud.put(name, payload)

    response_object = {
        "id": payload.id,
        "name": payload.name,
        "is_adopted": payload.is_adopted,
    }
    return response_object


@router.delete("/{name}/", response_model=DogDB)
async def delete_dog(name: str = Path(..., min_length=1)):
    dog = await crud.get(name)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    await crud.delete(name)

    return dog