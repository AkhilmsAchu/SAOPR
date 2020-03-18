from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.signin,name='index'),
    path('fetchproduct', views.fetchproduct,name='fetchproduct'),
    path('deleteproduct', views.deleteproduct,name='deleteproduct'),
    path('signin', views.signin,name='signin'),
    path('addproduct', views.addproduct,name='addproduct'),
    path('analyse', views.analyse,name='analyse'),
    path('signup', views.signup,name='signup'),
    path('home', views.home,name='home'),
]