from django.shortcuts import render
from ninja import Router

router = Router()


@router.get("/hello")
def hello(request):
    return {"message": "Hello, World!","status":200}

# Create your views here.
