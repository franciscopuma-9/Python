from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/user",tags=["user"])


#Entidad user

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int


users_list = [User(id=1,name ='Fran',surname='Puma',url="franpuma@gmail.com",age= 23),
         User(id=2,name ='Cami',surname='Galarza',url="cami@gmail.com",age=23),
         User(id=3,name ='Santi',surname='Malbran',url="santi@gmail.com",age=24)]


@router.get('/json')
async def usersjson():
    return [{'name':'Fran','surname':'Puma',"url":"franpuma@gmail.com",'age':23},
            {'name':'Cami','surname':'Galarza',"url":"camigalarza@gmail.com",'age':23},
            {'name':'Santi','surname':'Malbran',"url":"santimalbran@gmail.com",'age':24}]


@router.get('/users')
async def users():
    return users_list

#Path
@router.get('/{id}')
async def user(id:int):
    users = filter(lambda user: user.id == id,users_list)

    #operaciones complejas y devolver su resultado
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

#Query
@router.get('/query')   #/userquery/?id=1
async def user(id:int):
    users = filter(lambda user: user.id == id,users_list)

    #operaciones complejas y devolver su resultado
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

#crear dato
@router.post("/",status_code=201)
async def user(user: User):
    #raise HTTPException(status_code=204, detail="el usuario ya existe") # HTTP Status Code
    users_list.append(user)
    return user


#actualizar dato
@router.put("/")
async def user(user:User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha encontrado el usuario"}
    else:
        return {"Eliminacion":"Se elimino correctamente"}

