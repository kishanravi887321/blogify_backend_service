from urllib import request
from django.shortcuts import render
from ninja import Router,Schema
from django.contrib.auth import authenticate,get_user_model

router = Router()
User = get_user_model()
# // making the doctor route for check

@router.get("/doctor")
def doctor(request):
    return {"message":"The API is working fine"}



class RegisterS(Schema):
    username: str
    email: str
    password: str
    fullname: str
    bio: str


@router.post("register/")
def register(request, data: RegisterS):

    user = User(
        username=data.username,
        email=data.email,
        fullname=data.fullname,
        bio=data.bio
    )
    user.set_password(data.password)
    user.save()
    return {"message": "User registered successfully", "user": {
        "username": user.username,
        "email": user.email,
        "fullname": user.fullname,
        "bio": user.bio,
        "password":user.password
    }, "status": 200}



class LoginS(Schema):
    email:str
    password:str

@router.post("login/")
def login(request,data:LoginS):
    user = authenticate(request,email=data.email, password=data.password)
    if user:
        return {"message": "Login successful", "user": {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "bio": user.bio
        }, "status": 200}
    return {"message": "Invalid credentials", "status": 401}


