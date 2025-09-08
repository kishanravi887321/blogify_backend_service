import jwt
import datetime
import  os 
from dotenv import load_dotenv
load_dotenv()
from ninja.errors import HttpError

# Make sure you have a secret key in settings.py
JWT_SECRET = os.getenv("JWT_TOKEN_SECRET")
ALGORITHM = os.getenv("TOKEN_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_LIFE_TIME")
REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("JWT_REFRESH_LIFE_TIME")


def create_access_token(payload: dict) -> str:
    to_encode = payload.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


def create_refresh_token(payload: dict) -> str:
    to_encode = payload.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=int(REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HttpError(401, "Token has expired")
    except jwt.InvalidTokenError:
        raise HttpError(401, "Invalid token")


def refresh_access_token(refresh_token: str) -> str:
    payload = decode_token(refresh_token)
    if payload.get("type") != "refresh":
        raise HttpError(401, "Invalid refresh token type")
    # issue new access token using same user payload
    new_payload = {"email": payload["email"]}
    return create_access_token(new_payload)

