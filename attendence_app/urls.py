from django.contrib import admin
from django.urls import path
from attendence_app import views
urlpatterns = [
    path('',views.home, name= 'home'),
    
    path('loginStaff',views.loginStaff, name= 'loginStaff'),
    path('loginStudent',views.loginStudent, name= 'loginStudent'),
    path('logout',views.logoutUser, name= 'logout'),
    path('home',views.home, name= 'home'),
    path('profile',views.profile, name= 'profile'),
    path('attendance',views.attendance, name= 'attendance'),
    
]