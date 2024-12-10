from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from hello import models


def get_user(request, name):
    user = ""
    return JsonResponse({"user": user})


##User
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

    if user is not None:
        return JsonResponse({"result": "Success"})

    return JsonResponse({"result": "Invalid credentials"}, status=401)


def sign_up(request):
    username = request.GET.get("username")
    email = request.GET.get("email")
    password = request.GET.get("password")

    if models.UserModel.objects.filter(username=username).first():
        return JsonResponse({"result": "Username taken"}, status=409)

    if models.UserModel.objects.filter(email=email).first():
        return JsonResponse({"result": "Email taken"}, status=409)

    if not username or not email or not password:
        return JsonResponse({"result": "Invalid input"}, status=400)

    models.UserModel.objects.create(
        username=username,
        email=email,
        password=password
    )
    return JsonResponse({"result": "Success"})


##Lines
def get_lines(request):
    lines = models.LineModel.objects.all()
    res = []
    for line in lines:
        line_res = line.to_dict()
        stations = (
            models
            .StationModel
            .objects
            .filter(line=line)
            .order_by("num")
        )
        line_res["stations"] = list(map(str, stations))
        res.append(line_res)

    return JsonResponse({"lines": res})


##Posts
def get_posts_from_station(request):
    station = request.GET("station")
    posts = models.PostModel.objects.filter(station=station)
    return JsonResponse({"posts": map(lambda post: post.to_dict(), posts)})


def get_posts_from_user(request):
    user = request.GET("user")
    posts = models.PostModel.objects.filter(user=user)
    return JsonResponse({"posts": map(lambda post: post.to_dict(), posts)})


def create_post(request):
    username = request.GET("username")
    station_name = request.GET("station")
    text = request.GET("text")
    photo = request.GET("photo")
    user = models.UserModel.objects.filter(username=username).first()
    station = models.StationModel.objects.filter(name=station_name).first()
    if user is None or station is None:
        return JsonResponse({"result": "Invalid input"}, status=400)
    models.PostModel.objects.create(
        user=user,
        station=station,
        text=text,
        photo=photo
    )
    return JsonResponse({"result": "Success"})
