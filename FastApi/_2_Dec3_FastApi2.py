import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

#Model to vaidate data
class Greetingmodel(BaseModel):
    texts:str

app =FastAPI()
@app.post('/send_greetings')
async def send_data(text:Greetingmodel):
    print(text.texts)
    return {"status":200}

uvicorn.run(app)
