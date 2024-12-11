"""
URL configuration for metro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse, HttpResponse
from django.urls import path

from hello.views import login, sign_up, get_lines, create_post, get_posts_from_station
from metro import settings

urlpatterns = [
    path("hello", lambda response: JsonResponse({"Hello": "Hello world!"})),
    path('', lambda response: HttpResponse('<h1><span style="color: red;">This</span> is a main page</h1>')),
    path('login', login),
    path('signup', sign_up),
    path('get_lines', get_lines),
    path('create_post', create_post),
    path('get_posts', get_posts_from_station),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

