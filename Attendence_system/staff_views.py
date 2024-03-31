from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
@login_required(login_url='index.html')

def HOME(request):
    return render(request,'staff/home2.html')