from app.api import crud
from app.api.models import DogSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/", status_code=201)
async def create_dog(payload: DogSchema):
    #dog_id = await crud.post(payload)

    response_object = {
        "id": payload.id,
        "name": payload.name,
        "picture": payload.picture,
        "is_adopted": payload.is_adopted,
    }
    return response_object