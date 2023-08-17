from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from courses.views import home,coursePage,CreateForm,checkout,verifyPayment
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# def home(request):
#     return HttpResponse("Home page")
app_name="courses"
urlpatterns = [
    
    path('',home,name='home'),
    path('signup/',CreateForm.as_view(),name='signup'),
    path('course/<str:slug>',coursePage,name='coursePage'),
    path('check-out/<str:slug>',checkout,name='check-out'),
    path('login/',auth_views.LoginView.as_view(template_name='courses/login.html'),name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('verify_payment',verifyPayment,name='verify_payment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)