from .routes  import  router

from django.urls import path

urlpatterns = [
    path("blog/", router.urls)]
