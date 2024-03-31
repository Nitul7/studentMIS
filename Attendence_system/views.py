from django.shortcuts import render,redirect,HttpResponse
from attendence_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'index.html')

def faclogin(request):
    if request.method=="POST":
        user=EmailBackEnd.authenticate(request,
            username=request.POST.get('email'),
            password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('staff_home')
            elif user_type == '2':
                return HttpResponse('This is staff panel')
            else:
                return redirect('login')
        else:
            return redirect('login')
        
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')
        
