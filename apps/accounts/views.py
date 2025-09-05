from urllib import request
from django.shortcuts import render
from typing import Optional
from ninja import File, Form
from ninja.files import UploadedFile
import cloudinary.uploader
from ninja import Router, Schema
from django.conf import settings
from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth import authenticate, get_user_model
from auth.auth_tokens import (
    create_access_token,
    create_refresh_token,
    decode_token,
    refresh_access_token,
)
from ..services.otpservices.otp_sender_clean import (
    RegistrationOtpSender,
    WelcomeEmailSender,
    ForgetPasswordOtpSender,
    LoginOtpSender,
)
from django.core.cache import cache
from .backend import JWTAuth

router = Router()
User = get_user_model()


# // doctor check route
@router.get("/doctor")
def doctor(request):
    return {"message": "The API is working fine"}


# ==================== REGISTER ====================
class RegisterS(Schema):
    username: str
    otp: str
    email: str
    password: str
    fullname: str
    bio: str


@router.post("/register")
def register(request, data: RegisterS):
    username = data.username.strip()
    email = data.email.strip()
    fullname = data.fullname.strip()
    bio = data.bio.strip() if data.bio else ""

    if User.objects.filter(email=email).exists():
        return {"message": "This email already exists", "status": 400}

    if User.objects.filter(username=username).exists():
        return {"message": "This username already exists", "status": 400}

    if not data.otp:
        return {"message": "OTP is required", "status": 400}
    if not cache.get(f"otp:register:{email}")==data.otp.strip():
        return {"message": "Invalid or expired OTP", "status": 403}

    user = User(
        username=username,
        email=email,
        fullname=fullname,
        bio=bio,
    )
    user.set_password(data.password.strip())
    user.save()
    welcome_greet=WelcomeEmailSender(user.email,user.username)
    welcome_greet.send()

    return {
        "message": "User registered successfully",
        "user": {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "bio": user.bio,
        },
        "status": 200,
    }


# ==================== LOGIN ====================
class LoginS(Schema):
    email: str
    password: str


@router.post("/login")
def login(request, data: LoginS):
    email = data.email.strip()
    password = data.password.strip()

    user = authenticate(request, email=email, password=password)
    print(user)

    if user:
        access_token = create_access_token(
            {"email": user.email, "name": user.fullname, "user_id": user.id}
        )
        refresh_token = create_refresh_token(
            {"email": user.email, "name": user.fullname, "user_id": user.id}
        )
        return {
            "message": "Login successful",
            "user": {
                "username": user.username,
                "email": user.email,
                "fullname": user.fullname,
                "bio": user.bio,
                "profile": user.profile,
                "cover": user.cover,
            },
            "access_token": access_token,
            "refresh_token": refresh_token,
            "status": 200,
        }
    return {"message": "Invalid credentials", "status": 401}


# ==================== GOOGLE LOGIN ====================
class GoogleLoginS(Schema):
    id_token: str


@router.post("/google-login")
def google_login(request, data: GoogleLoginS):
    try:
        idinfo = google_id_token.verify_oauth2_token(
            data.id_token.strip(),
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID,
        )

        email = idinfo.get("email", "").strip()
        name = idinfo.get("name", "").strip()

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": email.split("@")[0],
                "fullname": name,
            },
        )

        access_token = create_access_token(
            {"email": user.email, "name": user.fullname, "user_id": user.id}
        )
        refresh_token = create_refresh_token(
            {"email": user.email, "name": user.fullname, "user_id": user.id}
        )

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
            "status": 200,
        }

    except ValueError:
        return {"message": "Invalid Google ID token", "status": 401}


# ==================== REFRESH TOKEN ====================
class RefreshS(Schema):
    refresh_token: str


@router.post("/refresh")
def refresh(request, data: RefreshS):
    try:
        new_access_token = refresh_access_token(data.refresh_token.strip())
        return {"access_token": new_access_token, "status": 200}
    except Exception as e:
        return {"message": f"Invalid refresh token: {str(e)}", "status": 401}


# ==================== UPDATE PROFILE ====================


class UpdateProfileS(Schema):
    username: Optional[str] = None
    fullname: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    social_links: Optional[dict] = None


@router.patch("/update-profile", auth=JWTAuth())
def update_profile(
    request,
    data: UpdateProfileS = Form(...), 
    profile: UploadedFile = File(None),
    cover: UploadedFile = File(None),
):
    user = request.auth
    update_fields = []

    if data.username is not None:
        username = data.username.strip()
        if User.objects.filter(username=username).exclude(id=user.id).exists():
            return {"message": "Username already taken", "status": 401}
        user.username = username
        update_fields.append("username")

    if data.fullname is not None:
        user.fullname = data.fullname.strip()
        update_fields.append("fullname")

    if data.bio is not None:
        user.bio = data.bio.strip()
        update_fields.append("bio")

    if data.location is not None:
        user.location = data.location.strip()
        update_fields.append("location")

    # ✅ Upload profile image to Cloudinary
    if profile is not None:
        upload_result = cloudinary.uploader.upload(profile.file, folder="profiles")
        user.profile = upload_result["secure_url"]
        update_fields.append("profile")

    # ✅ Upload cover image to Cloudinary
    if cover is not None:
        upload_result = cloudinary.uploader.upload(cover.file, folder="covers")
        user.cover = upload_result["secure_url"]
        update_fields.append("cover")

    if data.social_links is not None:
        user.social_links = data.social_links
        update_fields.append("social_links")

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
            "social_links": user.social_links,
        },
        "status": 200,
    }



# ==================== GET PROFILE ======================
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
            "social_links": user.social_links,
        },
        "status": 200,
    }


# ==================== CHANGE PASSWORD ====================
class UpdatePassS(Schema):
    old_password: str
    new_password: str


@router.post("/change-password", auth=JWTAuth())
def change_password(request, data: UpdatePassS):
    user = request.auth
    if not user.check_password(data.old_password.strip()):
        return {"message": "Old password is incorrect", "status": 401}
    user.set_password(data.new_password.strip())
    user.save()
    return {"message": "Password changed successfully", "status": 200}


# ==================== FORGET PASSWORD ====================
class ForgetPassS(Schema):
    email: str
    otp: str
    new_password: str


@router.post("/forget-password")
def forget_password(request, data: ForgetPassS):
    email = data.email.strip()
    otp = data.otp.strip()
    new_password = data.new_password.strip()

    user = User.objects.filter(email=email).first()
    if not user:
        return {"message": "User not found", "status": 401}

    if cache.get(f"otp:forget:{email}") != otp:
        return {"message": "Invalid or expired OTP", "status": 402}

    

    user.set_password(new_password)
    user.save()
    return {"message": "Password reset successfully", "status": 200}


# ==================== AUTH FORGET PASSWORD ====================
class ForgetPasswordOtpS(Schema):
    email: str


@router.post("/auth-forget-password")
def auth_forget_password(request, data: ForgetPasswordOtpS):
    email = data.email.strip()
    user = User.objects.filter(email=email).first()
    if not user:
        return {"message": "User not found", "status": 401}

    otp_sender = ForgetPasswordOtpSender(user.email)
    otp_sender.send()

    return {"message": "OTP sent to email", "status": 200}

class RegistrationOtpS(Schema):
    email: str
@router.post("/auth-register")
def auth_registration(request, data: RegistrationOtpS):
    email = data.email.strip()
    user = User.objects.filter(email=email).first()
    if  user:
        return {"message": "User already exists", "status": 401}

    otp_sender = RegistrationOtpSender(data.email)
    otp_sender.send()

    return {"message": "OTP sent to email", "status": 200}



