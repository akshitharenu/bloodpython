
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse





class UserRegistration(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.IntegerField()

    def get_url(self):
        return reverse('blood:registerView',args=[self.name])
    def __str__(self):
        return self.name
class userLogin(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.IntegerField()



    def __str__(self):
        return self.name




