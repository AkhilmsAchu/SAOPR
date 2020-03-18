from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Products
from django.forms import ModelForm
#from farmers.models import Article
# Create your views here.
class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name','url']


def fetchproduct(request):
	product=Products.objects.filter()
	return render(request,"home/analyse.html",{'product':product})

def deleteproduct(request):
	pid = request.GET['id']
	try:
		chkprdt=Products.objects.get(id=pid)
	except Products.DoesNotExist:
		chkprdt = None
	if chkprdt:
		try:
			chkprdt.delete()
			return redirect(r'/analyse')
		except:
			print('Something went wrong, TryAgain')
	else:
		print('No such Product in Cart')

def analyse(request):
	product=Products.objects.filter()
	return render(request,"home/analyse.html",{'product':product})


def addproduct(request):
	form = AddProductForm(request.POST or None)
	context={
		'form':form
		}
	if request.method == 'POST':
		
		if form.is_valid():
			instance = form.save()
			return redirect(r'/home')
		else:
			form = AddProductForm(request.POST or None)
			context={
			'form':form
			}
			return render(request,"home/products.html",context)
	else :
		form = AddProductForm()
		context={
		'form':form
		}

	return render(request,"home/products.html",context)


def home(request):
	return render(request,"home/base.html")

def signin(request):
	if request.method == 'POST':
		
		username=request.POST['username']
		password = request.POST['password']
		user=auth.authenticate(username=username,password=password)
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
