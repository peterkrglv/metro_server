from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from hello import models


# Create your views here.


# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request, name="nameless"):
#     return HttpResponse(f"<h2>Имя: {name}</h2>")
#
# def coffee(request):
#     cof = request.GET.get("type", "Espresso")
#     return JsonResponse({"coffee": cof})

def get_user(request, name):
    user = ""
    return JsonResponse({"user": user})

def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")

    user = (
        models
        .UserModel
        .objects
        .filter(username=username, password=password)
        .first()
    )

    return JsonResponse({"result": user is not None})



