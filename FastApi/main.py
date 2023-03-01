from fastapi import FastAPI
from routers import products,users
from fastapi.staticfiles import StaticFiles

app = FastAPI()


#Routers
app.include_router(products.router)
app.include_router(users.router)

#Montar recursos estaticos
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get('/') #el root
async def root():
    return "Hola FastAPI!"


@app.get('/key') #path
async def key():
    return {"key":"value"}