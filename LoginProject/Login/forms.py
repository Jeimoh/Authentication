from django.forms import ModelForm
from .models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # You don't want to register using all fields, since this will display even the auto-filled fields
        # You should use the following
