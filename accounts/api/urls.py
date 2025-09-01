from .routes import  router

from django.urls import path

urlpatterns = [
    path("", router.urls)]
