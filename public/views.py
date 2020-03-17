from django.shortcuts import render
from django.shortcuts import render, redirect

def signin(request):
	return render(request,"public/signin.html")

def signup(request):
	return render(request,"public/signup.html")


# Create your views here.
