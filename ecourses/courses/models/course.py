from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name=models.CharField(max_length=50,null=False)
    slug=models.CharField(max_length=50,null=False,unique=True)
    discription =models.CharField(max_length=2000,null=True)
    price=models.IntegerField(null=False)
    discount=models.IntegerField(null=False,default=0)
    active=models.BooleanField(default=False)
    thumbnail=models.ImageField(upload_to="files/thumbnail")
    date=models.DateTimeField(auto_now_add=True)
    resource=models.FileField(upload_to='files/resource')
    length=models.IntegerField(null=False)
    def __str__(self) -> str:
        return self.name
    
class CourseProperty(models.Model):
    discription=models.CharField(max_length=100,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    
    class Meta():
        abstract=True
    
    
class Tag(CourseProperty):
    pass
    
class Prerequisite(CourseProperty):
    pass
    
class Learning(CourseProperty):
    pass

class Customuser(AbstractUser):
    email=models.EmailField()


    def __str__(self):
       return self.username
   