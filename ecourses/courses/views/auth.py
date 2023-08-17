from django.shortcuts import render, get_object_or_404
from courses.models import Course, Vedio
from django.http import HttpResponse
from courses.forms import Form
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.contrib.auth import views
# from django.contrib.auth.forms import UserCreationForm

class CreateForm(CreateView):
    form_class = Form
    success_url = reverse_lazy('courses:user_login')
    template_name = 'courses/signup.html'