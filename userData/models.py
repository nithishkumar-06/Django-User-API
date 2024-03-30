from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length = 100, unique=True)
    password = models.CharField(max_length=16)
    phone = models.IntegerField()
    def __str__(self):
        return self.userName