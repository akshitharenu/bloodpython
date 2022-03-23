from django.contrib import messages, auth
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def base(request):
    return render(request, 'base.html')


def loginView(request, user=None):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirm password']



        return redirect('register')



    return render(request, "login.html")

def registerView(request, user=None):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm password']


        return redirect('blood form')

    return render(request,"register.html")


def bloodForm(request, user=None):
    if request.method == 'POST':
        name = request.POST['username']
        age = request.POST['age']
        gender = request.POST['gender']
        gender = request.POST['gender']
        address = request.POST['address']

        Phonenumber = request.POST['phone number']
        if User is not None:
            auth.login(request, user)
            messages.info(request, "registration done successfully")


    return render(request,"blood form.html")


def logoutView(request):

    auth.logout(request)
    return redirect('/')
