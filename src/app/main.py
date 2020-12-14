from fastapi import FastAPI

from app.api import dog, ping
from app.db.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(dog.router, prefix="/dog", tags=["dog"])