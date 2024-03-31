"""
URL configuration for Attendence_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,student_views,staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name= 'home'),
    path('faclogin',views.faclogin, name= 'faclogin'),
    
    path('staff/home2.html',staff_views.HOME,name='staff_home2'),
    path('staff/home.html',staff_views.HOME,name='staff_home'),


    path('logout',views.logout_request, name="logout")
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
