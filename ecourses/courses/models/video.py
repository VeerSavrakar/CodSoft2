from django.db import models
from courses.models import Course
class Vedio(models.Model):
    title=models.CharField(max_length=100,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number=models.IntegerField(null=False)
    vidio_id=models.CharField(max_length=100,null=False) 
    is_preview=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    