from fastapi import FastAPI

zekapi = FastAPI()

@zekapi.get('/main')
def index():
    return {"text":"Hello ZEK !"}