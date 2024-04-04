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
    path('attendence',views.attendence, name= 'attendence'),
    # path('index',views.index, name= 'index'),
    
    path('base',views.base, name= 'base'),
    
    # path('faclogin',views.faclogin, name= 'faclogin'),
    
    # path('staff/home2.html',views.HOME,name='staff_home2'),
    # path('staff/home.html',views.HOME,name='staff_home'),


    # path('logout',views.logout_request, name="logout"),
]