from urllib import request
from django.shortcuts import render
from typing import Optional
from ninja import Router,Schema
from django.conf import settings
from google.oauth2 import  id_token  as google_id_token
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
            "bio": user.bio,
            "profile":user.profile,
            "cover":user.cover
        }, "status": 200}
    return {"message": "Invalid credentials", "status": 401}


class GoogleLoginS(Schema):
    id_token: str

@router.post("google-login/")
def google_login(request, data: GoogleLoginS):
    token=data.get("id_token")
    try:
        import  requests
        idinfo = google_id_token.verify_oauth2_token(token,requests.Request(),settings.GOOGLE_CLIENT_ID)
        email=idinfo.get("email")
        print(email)

    except ValueError:
        raise ValueError({"message": "Invalid token", "status": 401})