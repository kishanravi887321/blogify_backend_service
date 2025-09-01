from django.shortcuts import render
from ninja import NinjaAPI
from django.contrib.auth import authenticate

router=NinjaAPI()


# // making the doctor route for check 

router.get("/doctor")
def doctor(req):
    return {"message":"The API is working fine"}
# Create your views here.
