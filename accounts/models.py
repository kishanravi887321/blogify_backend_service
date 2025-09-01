from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None ,**kwargs):

        if not email:
            raise ValueError("Users must have an email address")
        
        email=self.normalize_email(email)
        user=self.model(email=email,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email,password,**kwargs)
    

class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150,unique=True)
    fullname = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile=models.URLField(blank=True)
    cover=models.URLField(blank=True)
    social_links=models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
