from typing import List

from app.api import crud
from app.api.models import DogSchema, DogDB
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/",response_model=DogDB, status_code=201)
async def create_dog(payload: DogSchema):
    dog_id = await crud.post(payload)

    response_object = {
        "id": payload.id,
        "name": payload.name,
        "picture": payload.picture,
        "is_adopted": payload.is_adopted,
    }
    return response_object

@router.get("/{id}/", response_model=DogDB)
async def read_dog(id: str = Path(..., min_length=1),):
    dog = await crud.get(id)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog


@router.get("/", response_model=List[DogDB])
async def read_all_dogs():
    return await crud.get_all()


@router.put("/{id}/", response_model=DogDB)
async def update_dog(payload: DogSchema, id: str = Path(..., min_length=1),):
    dog = await crud.get(id)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    dog_id = await crud.put(id, payload)

    response_object = {
        "id": payload.id,
        "name": payload.name,
        "picture": payload.picture,
        "is_adopted": payload.is_adopted,
    }
    return response_object


@router.delete("/{id}/", response_model=DogDB)
async def delete_dog(id: str = Path(..., min_length=1)):
    dog = await crud.get(id)
    if not dog:
        raise HTTPException(status_code=404, detail="dog not found")

    await crud.delete(id)

    return dog