import re
from typing import List

from app.api.crud import user_crud
from app.models.models import UserSchema, UserDB, DogDB
from fastapi import APIRouter, HTTPException, Path


router = APIRouter()


@router.post("/addUser",response_model=UserDB, status_code=201)
async def create_user(payload: UserSchema):
    email_reg = re.compile("\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    user_exist_id = await user_crud.get_by_id(payload.id)
    if user_exist_id:
        raise HTTPException(status_code=409, detail="id already exists")
    if not email_reg.match(payload.email):
        raise HTTPException(status_code=422, detail="Bad email format, email must be someting@somenting.som")
    else:
        user_id = await user_crud.post(payload)
    response_object = {
        "id": payload.id,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "email": payload.email

    }
    return response_object



@router.get("/", response_model=List[UserDB])
async def read_all_users():
    return await user_crud.get_all()

@router.get("/{id}/", response_model=UserDB)
async def read_user(id: int = Path(..., gt=0),):
    user = await user_crud.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.put("/{id}/", response_model=UserSchema)
async def update_user(payload: UserSchema, id: int = Path(..., gt=0),):
    user = await user_crud.get_by_id(id)
    email_reg = re.compile("\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    if id != payload.id:
        raise HTTPException(status_code=422, detail="You can't change id")
    if not email_reg.match(payload.email):
        raise HTTPException(status_code=422, detail="Bad email format, email must be someting@somenting.som")
    else:
        user_id = await user_crud.put(id, payload)
    updated_user = await user_crud.get_by_id(id)

    return updated_user


@router.delete("/{id}/", response_model=UserDB)
async def delete_user(id: int = Path(..., gt=0)):
    user = await user_crud.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    await user_crud.delete(id)

    return user

@router.get("/get_adopted/{id}/", response_model=List[DogDB])
async def get_adopted_dogs(id: int = Path(..., gt=0),):
    user = await user_crud.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    return await user_crud.get_adopted_dogs(id)