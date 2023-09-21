from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory='E:\GeekBrains\Flask and FastAPI\Homework\homework5\\templates')

users = []


class User(BaseModel):
    id: int
    name: str
    mail: str
    password: str


class UserIn(User):
    pass


@app.post('/add_user/', response_model=list[User])
async def create_user(user: UserIn):
    users.append(User(id=len(users) + 1, name=user.name,
                 mail=user.mail, password=user.password))
    return users


@app.put('/update_user/{id}')
async def update_user(id: int, user: UserIn):
    try:
        usr = users[id - 1]
        usr.name = user.name
        usr.mail = user.mail
        usr.password = user.password
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User id-{id} not found')
    return usr


@app.delete('/delete_user/')
async def del_user(id: int):
    try:
        users.remove(users[id - 1])
        return {'message': f'User id-{id} is deleted'}
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f'User id-{id} not found')
    

@app.get('/users/', response_class=HTMLResponse)
async def get_user(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
