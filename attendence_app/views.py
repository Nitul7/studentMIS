from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from attendence_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from attendence_app.models import *
from .models import *

# @login_required(login_url='/')
# @login_required(login_url='login.html')

def loginStaff(request):
    # student: @student00 ,123happy@123
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        # check if user is valid
        user = authenticate(username=username, password=password)
        if user is not None:# if the user is logged in
            login(request,user)
            if request.user.is_superuser:
                return redirect ('/')
            else:
                logout(request)
                return redirect ('/')
        else:# if the user is not logged in
            return render (request,"login.html")
    return render (request,'login.html')

def loginStudent(request):
    # student: @student00 ,123happy@123
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        # check if user is valid
        user = authenticate(username=username, password=password)
        if user is not None:# if the user is logged in
            login(request,user)
            if request.user.is_superuser:
                logout(request)
                return redirect ('/')
            else:
                return redirect ('/')
        else:# if the user is not logged in
            return render (request,"login.html")
    return render (request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect ('/loginStudent')

def home(request):
    if request.user.is_anonymous:
        return redirect("/loginStudent")
    else:
        if request.user.is_superuser:
            context = {
                "attendences": Attendence.objects.all()
            }
            return render (request,"staff_index.html",context)
        else:
            return render (request,"student_index.html")
        
def base(request):
    return render(request, "base.html")


def profile(request):
    current_user = request.user
    # return HttpResponse(current_user.first_name)
    context = {
        'records':Students.objects.filter(user_name = current_user),
        'staff_records':current_user
    }
    return render (request,"profile.html",context)

def attendance(request):
    main_context = {
        "subjects": Subjects.objects.all()
    }
    if request.method == "POST":
        sub_sem = request.POST.get("subject_semister")
        sub_name = request.POST.get("subject_name")
        if sub_sem is not None:  # Check if sub_sem is not None
            semester = int(sub_sem)
            students = Students.objects.filter(current_semister=semester)
            context = {
                "students": students
            }
            for student in students:
                is_present = request.POST.get(student.roll)
                # print(f"Value of is_present for {student.roll}: {is_present}")
                # return HttpResponse(f" It isS: {is_present}")
                if is_present == "True":
                    attendance_record, _ = Attendence.objects.get_or_create(student=student)
                    attendance_record.present_days += 1
                    attendance_record.save()
            return render(request, "take_attendance.html", context)
        else:
            return HttpResponse("Semester not provided.")
    else:
        return render(request, "select_attendance.html", main_context)



# def faclogin(request):
#     if request.method=="POST":
#         user=EmailBackEnd.authenticate(request,
#             username=request.POST.get('email'),
#             password=request.POST.get('password'),)
#         if user!=None:
#             login(request,user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('staff_home')
#             elif user_type == '2':
#                 return HttpResponse('This is staff panel')
#             else:
#                 return redirect('login')
#         else:
#             return redirect('login')
        
# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return render(request,'index.html')
        




# def HOME(request):
#     return render(request,'staff/home2.html')