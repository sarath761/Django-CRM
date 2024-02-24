from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
from django.shortcuts import get_object_or_404

def home(request):
    if request.user.is_authenticated:
        
        records = Record.objects.filter(user=request.user)
    else:
        records = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully.")
            
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        
        customer_record = get_object_or_404(Record, pk=pk, user=request.user)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view that page.")
        return redirect('home')





def delete_record(request, pk):
    if request.user.is_authenticated:
        
        delete_it = get_object_or_404(Record, id=pk, user=request.user)
        delete_it.delete()
        messages.success(request, "Record deleted successfully.")
    else:
        messages.error(request, "You must be logged in to do that.")
    return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                
                add_record = form.save(commit=False)
                add_record.user = request.user
                add_record.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to do that.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record, id=pk, user=request.user)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully.")
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to do that.")
        return redirect('home')


