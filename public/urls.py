from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.signin,name='index'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
]