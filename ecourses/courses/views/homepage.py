from django.shortcuts import render
# from django.http import HttpResponse
from courses.models import Course

def home(request):
    courses=Course.objects.all()
    print(courses)
    return render(request,'courses/home.html',{"courses":courses})
    

