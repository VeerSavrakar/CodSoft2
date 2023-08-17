from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from courses.models import Customuser

class Form(UserCreationForm):
    class Meta:
        model = Customuser
        fields = ['username', 'email', 'password1', 'password2']
