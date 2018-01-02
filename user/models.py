from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

