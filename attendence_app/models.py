from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER=(
        ('1','STAFF'),
        ('2','STUDENT'),
    )
    user_type= models.CharField(choices=USER,max_length=50,default=1)

# class Attend(models.Model):
    # 123happy@123
#     fname
#     lname
#     roll 
#     email