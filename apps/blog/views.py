from django.shortcuts import render
from ninja  import  Router,Schema
from django.contrib.auth import authenticate



router=Router(tags=["Blog"])


# Create your views here.

@router.get("/hello")
def hello(request):
    return  {"message":"Hello World from Blog app","status":202}