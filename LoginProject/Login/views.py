from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.
def RegisterUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('REGISTERED USER SUCCESSUL')
        else:
            form = RegisterForm()
 
    context = {'form':form}
    return render(request, 'Login/Register.html',context)
def LoginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Made the changes in the login field names
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Login Successful')
            else:
                return HttpResponse('invalid username or password')  
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'Login/login.html',context)