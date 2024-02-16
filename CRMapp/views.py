from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Your are login successful") 
            return redirect('home')
        else:
            messages.success(request,"Enter Login Credentials Correctly")
            return redirect('home')
    else:
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')



def register_user(request):
    
    
    return render(request,'register.html',{})


