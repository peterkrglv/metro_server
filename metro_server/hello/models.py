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
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=511)
    password = models.CharField(max_length=255)

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

class LineModel(models.Model):
    name = models.CharField(max_length=63, default='')
    color = models.IntegerField(default=0)
    #stations = ArrayField(models.CharField(max_length=63))

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color
        }

    # Line -> Stations
    # {
    #  [
    #      "Red" : ["Boulevard Rokossovskogo", "Krasnoselskaya"...],
    #      "Blue" : ["Krasnye Vorota", "Krasnoselskaya"...],
    #  ]
    # }


class PostModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    station = models.CharField(max_length=63)
    text = models.CharField(max_length=2047)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos", blank=True)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "station": self.station,
            "text": self.text,
            "date": self.date,
            "photo": self.photo
        }
