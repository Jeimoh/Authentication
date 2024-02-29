from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from .models import Users

# Create your views here.
def RegisterUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
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
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data['password']
            user = authenticate(request,username=Username, password=Password)
            if user is not None:
                login(request, user)
                return HttpResponse('Login Successful')
            else:
                return HttpResponse('invalid username or password')  
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'Login/login.html',context)