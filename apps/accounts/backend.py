from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from ninja.security import HttpBearer
User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, req, email=None, password=None):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None



class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        payload = decode_token(token)
        if payload and payload.get("type") == "access":
            try:
                user = User.objects.get(id=payload["user_id"])
                return user   # <-- returning the user object
            except User.DoesNotExist:
                return None
        return None