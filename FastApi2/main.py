from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return "Este es el home"

@app.get('/message')
async def message():
    return {"message": "Hello world"}

