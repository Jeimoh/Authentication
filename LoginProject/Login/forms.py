from django.forms import ModelForm
from .models import Users

class LoginForm(ModelForm):
    class Meta:
        model = Users
        fields = ['Username','password']
class RegisterForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
