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


class UpdateProfileS(Schema):
    username: Optional[str] = None
    fullname: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    profile: Optional[str] = None
    cover: Optional[str] = None
    social_links: Optional[dict] = None


@router.patch("/update-profile", auth=JWTAuth())
def update_profile(request, data: UpdateProfileS):
    user = request.auth
    
    # Update only the fields that are provided
    update_fields = []
    
    if data.username is not None:
        # Check if username is already taken by another user
        if User.objects.filter(username=data.username).exclude(id=user.id).exists():
            return {"message": "Username already taken", "status": 401}
        user.username = data.username
        update_fields.append('username')
    
    if data.fullname is not None:
        user.fullname = data.fullname
        update_fields.append('fullname')
    
    if data.bio is not None:
        user.bio = data.bio
        update_fields.append('bio')
    
    if data.location is not None:
        user.location = data.location
        update_fields.append('location')
    
    if data.profile is not None:
        user.profile = data.profile
        update_fields.append('profile')
    
    if data.cover is not None:
        user.cover = data.cover
        update_fields.append('cover')
    
    if data.social_links is not None:
        user.social_links = data.social_links
        update_fields.append('social_links')
    
    # Save only if there are fields to update
    if update_fields:
        user.save(update_fields=update_fields)
        
    return {
        "message": "Profile updated successfully",
        "user": {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "bio": user.bio,
            "location": user.location,
            "profile": user.profile,
            "cover": user.cover,
            "social_links": user.social_links
        },
        "status": 200
    }


@router.get("/profile", auth=JWTAuth())
def get_profile(request):
    user = request.auth
    return {
        "user": {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "bio": user.bio,
            "location": user.location,
            "profile": user.profile,
            "cover": user.cover,
            "social_links": user.social_links
        },
        "status": 200
    }



class UpdatePassS(Schema):
    old_password: str
    new_password: str

@router.post("/change-password", auth=JWTAuth())
def change_password(request, data: UpdatePassS):
    user = request.auth
    if user.check_password(data.old_password) is False:
        return {"message": "Old password is incorrect", "status": 401}
    user.set_password(data.new_password)
    user.save()
    return {"message": "Password changed successfully", "status": 200}


class ForgetPassS(Schema):
    email: str
    otp: str
    new_password: str

@router.post("/forget-password")
def forget_password(request, data: ForgetPassS):
    user = User.objects.filter(email=data.email).first()
    if not user:
        return {"message": "User not found", "status": 401}
 
    user.set_password(data.new_password)
    user.save()
    return {"message": "Password reset successfully", "status": 200}