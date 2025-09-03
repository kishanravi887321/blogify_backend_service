from urllib import request
from django.shortcuts import render
from typing import Optional
from ninja import Router,Schema
from django.conf import settings
from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth import authenticate,get_user_model
from auth.auth_tokens import create_access_token,create_refresh_token,decode_token,refresh_access_token
router = Router()
from .backend import JWTAuth
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


@router.post("/register")
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

@router.post("/login")
def login(request,data:LoginS):
    user = authenticate(request,email=data.email, password=data.password)
    
    if user:
        access_token = create_access_token({"email": user.email,"name":user.fullname, "user_id": user.id})
        refresh_token = create_refresh_token({"email": user.email,"name":user.fullname, "user_id": user.id})  
        return {"message": "Login successful", "user": {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "bio": user.bio,
            "profile":user.profile,
            "cover":user.cover
        }, "access_token": access_token, "refresh_token": refresh_token, "status": 200}
    return {"message": "Invalid credentials", "status": 401}


class GoogleLoginS(Schema):
    id_token: str

@router.post("/google-login")
def google_login(request, data: GoogleLoginS):
    try:
        # Verify Google token
        idinfo = google_id_token.verify_oauth2_token(
            data.id_token, 
            google_requests.Request(), 
            settings.GOOGLE_CLIENT_ID
        )

        email = idinfo.get("email")
        name = idinfo.get("name", "")
       

        # Find or create user
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": email.split("@")[0],  # or generate random
                "fullname": name,
              
            }
        )

        # Generate JWT tokens
        access_token = create_access_token({
            "email": user.email,
            "name": user.fullname,
            "user_id": user.id
        })
        refresh_token = create_refresh_token({
            "email": user.email,
            "name": user.fullname,
            "user_id": user.id
        })

        return {
            "message": "Google login successful",
            "user": {
                "username": user.username,
                "email": user.email,
                "fullname": user.fullname,
                "profile": user.profile,
                "cover": getattr(user, "cover", None),
                "bio": getattr(user, "bio", None),
            },
            "access_token": access_token,
            "refresh_token": refresh_token,
            "new_user": created,
            "status": 200
        }

    except ValueError:
        return {"message": "Invalid Google ID token", "status": 401}
class RefreshS(Schema):
    refresh_token: str

@router.post("/refresh")
def refresh(request, data: RefreshS):
    try:
        # Use the existing refresh_access_token function
        new_access_token = refresh_access_token(data.refresh_token)
        return {"access_token": new_access_token, "status": 200}
    except Exception as e:
        return {"message": f"Invalid refresh token: {str(e)}", "status": 401}




