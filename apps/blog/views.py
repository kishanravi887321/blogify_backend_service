from django.shortcuts import render
from ninja  import  Router,Schema



route=Router()


# Create your views here.

@route.get("/hello")
def hello(request):
    return  {"message":"Hello World from Blog app","status":202}