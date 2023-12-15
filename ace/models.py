from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    course_img=models.FileField(upload_to='documents',default='image.jpg')
    course_name=models.CharField(max_length=30)
    course_content=models.TextField()
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    image=models.FileField(upload_to='documents',default='image.jpg')

