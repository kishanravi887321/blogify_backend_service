from .routes import  router

from django.urls import path

urlpatterns = [
    path("users/", router.urls)]