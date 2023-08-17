from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course,Payment,UserCourse
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from ecourses.settings import KEY_ID, KEY_SECRET
from time import time
import razorpay
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = None
    payment=None
    if not request.user.is_authenticated:
        return redirect(reverse('courses:user_login'))
    user = request.user

    action = request.GET.get('action')
    order = None
    error=None
    if action == 'create_payment':
        try:
            user_course=UserCourse.objects.get(user=user,course=course)
            error="You are Already Enrolled in this Course"
        except:
            pass
        if error is None:
            amount = int((course.price - (course.price * course.discount * 0.01)) * 100)
            currency = "INR"
            notes = {
                "email": user.email,
                "name": f'{user.first_name} {user.last_name}'
            }
            receipt = f"ecourses-{int(time())}"
            order = client.order.create({
                'receipt': receipt,
                'notes': notes,
                'amount': amount,
                'currency': currency
            })
            payment=Payment()
            payment.user=user
            payment.order_id=order.get('id')
            # payment.user_course=
            payment.course=course
            payment.save()
    context = {
        "course": course,
        "order": order,
        "payment":payment,
        "error":error,
    }
    return render(request, 'courses/check-out.html', context=context)

@csrf_exempt
def verifyPayment(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        context={}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id=data['razorpay_order_id']
            razorpay_payment_id=data['razorpay_payment_id']
            payment=Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id=razorpay_payment_id
            payment.status=True
            usercourse=UserCourse(user=payment.user,course=payment.course)
            usercourse.save()
            print("Usercourse",usercourse)
            payment.user_course=usercourse
            payment.save()
            return render(request,'courses/mycourses.html',context=context)
        except:
            return HttpResponse("Sorry, there was an error.")
    