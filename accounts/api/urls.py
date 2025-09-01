from ..views import  router

from django.urls import path

urlpatterns = [
    path("", router.urls)]
