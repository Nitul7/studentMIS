from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from attendence_app.models import *
# Register your models here.

class UserModel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Students)
admin.site.register(Attendence)
admin.site.register(Subjects)

