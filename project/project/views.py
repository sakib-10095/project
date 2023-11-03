from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from myapp.models import customUser
from myapp import EmailBackEnd
from django.contrib.auth import authenticate,login,logout


def signupPage(request):
    error_messages = {
        'password_error': 'password or confirm passsword not match',
    }
    if request.method == "POST":
        uname=request.POST.get("name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("confirmpassword")
        if pass1!=pass2:   
            messages.error(request,error_messages['password_error'])
        else:
            myuser=customUser.objects.create_user(username=uname,email=email,password=pass1)
            myuser.save()
            return redirect("loginPage")

    return render(request,"singup.html")


def loginPage(request):
    error_messages={
        'username_error': 'username requierd.',
        'password_error': 'password requierd.',
        'login_error': 'invalid username or password. please try again',
    }
    if request.method=='POST':
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        if not username:
            messages.error(request, error_messages['username_error'])
        elif not pass1:
            messages.error(request, error_messages['password_error'])
        else:
            user=EmailBackEnd.authenticate(request,username=username,password=pass1)
            if user is not None:
                login(request,user)
                user_type=user.user_type
                if user_type=='1':
                    return redirect("adminPage")
                elif user_type=='2':
                    return HttpResponse("teacherPage")
                elif user_type=='3':
                    return HttpResponse("studentPage")
                else:
                    return redirect("signupPage")
            else:
                messages.error(request, error_messages['login_error'])

        
    return render(request,"login.html")


def adminPage(request):

    return render(request,"myAdmin/adminhome.html")


def myProfilePage(request):

    user=request.user
    context={
        'user': user
    }

    return render(request,"myProfile.html",context)