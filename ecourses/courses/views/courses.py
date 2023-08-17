from django.shortcuts import render, get_object_or_404,redirect
from courses.models import Course, Vedio,UserCourse
from django.http import HttpResponse
from django.urls import reverse

def coursePage(request, slug):
    print(slug)
    print(request.user)
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    vedios = course.vedio_set.all().order_by("serial_number")
    
    video = None
    if serial_number:
        video = get_object_or_404(Vedio, serial_number=serial_number, course=course)
    if video and not video.is_preview:
        if not request.user.is_authenticated:
            return redirect('courses:user_login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect('courses:check-out', slug=course.slug)
    context = {
        "course": course,
        "vedio": video,
        "vedios": vedios,
    }
    return render(request, 'courses/course_page.html', context=context)
