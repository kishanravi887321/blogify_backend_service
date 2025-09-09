from .routes import router
from django.urls import path
urlpatterns = [
    path("pipeline/", router.urls)]