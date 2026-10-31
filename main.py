from fastapi import FastAPI, status, HTTPException  
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="UserDemo")

users = []

class User(BaseModel):
    id : int
    name : str
    email : str
    age : int
    password : str

class UserResponse(BaseModel):
    id : int
    name : str
    email : str
    age : int

#status code - 201 
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    users.append(user)
    return {
        "message" : "User Created",
        "data" : user 
    }

#response model 
@app.get("/get_all_users", response_model=UserResponse)
def get_all_users():
    return {
        "status" : "Success",
        "message" : "Users fetched",
        "data" : users
    }

#custom exception - invalid id 
class InvalidIdException(Exception):
    def __init__(self, id:int):
        self.id = id

@app.get("/get_user/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user.id != user_id:
            #raising HTTPException 
            raise HTTPException(
                    status_code = 404,
                    detail = "User Not Found"
                )    

        #raising custom exception 
        if user.id < 0:
            raise InvalidIdException(id)
    return user


