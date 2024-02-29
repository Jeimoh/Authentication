from django.urls import path
from . import views

urlpatterns = [
    #path('New/',views.RegisterUser, name='Register'),
    path('Log/',views.LoginUser, name='Login'),
]