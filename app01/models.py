from django.db import models

# Create your models here.

class User_Info(models.Model):
    # uid=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username+self.password

class Score_Info(models.Model):
    userID=models.ForeignKey(User_Info)
    java=models.FloatField(max_length=50)
    python=models.FloatField(max_length=50)

    def __str__(self):
        return self.userID+self.java+self.python

