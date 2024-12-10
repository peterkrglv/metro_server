from django.contrib.postgres.fields import ArrayField
from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserModel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=511, unique=True)
    password = models.CharField(max_length=255)

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }


class LineModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=63, unique=True, default="")
    color = models.IntegerField(default=0)

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color,
        }


class StationModel(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=63)
    line = models.ForeignKey(LineModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    # Line -> Stations
    # {
    #  [
    #      "Red" : ["Boulevard Rokossovskogo", "Krasnoselskaya"...],
    #      "Blue" : ["Krasnye Vorota", "Krasnoselskaya"...],
    #  ]
    # }


class PostModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    station = models.ForeignKey(StationModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=2047)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos", blank=True)

    def to_dict(self):
        return {
            "username": self.user.username,
            "text": self.text,
            "date": self.date,
            "photo": self.photo
        }
