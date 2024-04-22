from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER=(
        ('1','STAFF'),
        ('2','STUDENT'),
    )
    user_type= models.CharField(choices=USER,max_length=50,default=1)

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Subjects(BaseModel):
    subject = models.CharField(max_length=50)
    subject_faculty = models.CharField(max_length=25)
    subject_semister = models.CharField(max_length=10,default='2')
    def __str__(self):
        return self.subject

class Students(BaseModel):
    # 123happy@123
    user_name = models.OneToOneField(get_user_model(),related_name="student_username" ,on_delete=models.CASCADE)
    first_name = models.CharField( max_length = 30, default="world")
    last_name = models.CharField( max_length = 30, default="hello")
    roll = models.CharField( max_length = 6)
    batch = models.CharField(max_length=4,default=2078)
    student_faculty = models.CharField(max_length=25)
    student_programe = models.CharField(max_length=25) 
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    guardian = models.CharField(max_length=35)
    def __str__(self):
        return self.roll

class Attendence(BaseModel):
    roll = models.ForeignKey(Students,related_name='students',on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    present_days = models.IntegerField(default=0)
    total_days = models.IntegerField(default=0)
    # def __str__(self):
    #     return self.present_days

