from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def signin(request):
	if request.method == 'POST':
		
		username=request.POST['username']
		print(username)
		password = request.POST['password']
		user=auth.authenticate(username=username,password=password)
		
		print(password)
		if user is not None:
			auth.login(request,user)
			print("loggedin")
			return redirect('/home')
		else :
			return redirect('/signin')
	else:
		return render(request,"public/signin.html")

def signup(request):
	if request.method == 'POST':
		name=request.POST['name']
		email=request.POST['email']
		password = request.POST['password']
		username=request.POST['email']

		user =User.objects.create_user(username=username,first_name=name,email=email,password=password)
		user.save();
		print('created')
		return redirect('/signin')
	else:
		return render(request,"public/signup.html")


# Create your views here.
