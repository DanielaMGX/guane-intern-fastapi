from fastapi import FastAPI

from app.api.routes import dog
from app.db.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(dog.router, prefix="/dogs", tags=["dogs"])