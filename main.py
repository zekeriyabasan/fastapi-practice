from fastapi import FastAPI

zekapi = FastAPI()

@zekapi.get('/main')
def index():
    return {"text":"Hello ZEK !"}

@zekapi.delete('/{id}')
def delete(id):
    return{"id":id}