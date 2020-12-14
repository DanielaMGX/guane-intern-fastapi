from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}