from typing import ValuesView
from django.http.request import validate_host
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Customer
def datab(request):
    unames = ['Gopal']
    psws = ["gopalfinance@660"]
    name = []
    password = []
    name.append(request.POST["uname"])
    password.append(request.POST["psw"])
    if (name == unames) and ( password == psws):
        datas = Customer.objects.all()
        return render(request,'database.html',{'datas':datas})
    else:
        return render(request,'registration/login.html',{})
