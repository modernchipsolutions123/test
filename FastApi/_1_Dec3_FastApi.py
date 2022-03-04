import fastapi
from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    msg = 'Hai '
    return msg



uvicorn.run(app)


