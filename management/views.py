from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboaard_owner(request):
    return render(request, 'dashboard_owner.html')

def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        user = authenticate(request,phone_number=phone_number , password=password)
        if user :
            auth_login(request, user)
            if user.is_owner:
                return redirect('dashboard_owner')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid phone number or password')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeatpassword')
        user = CustomUser.objects.filter(phone_number=phone_number).exists
        if user :
            messages.error(request, 'User is already exists')
        if password != repeat_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        user = CustomUser.objects.create(name=name, phone_number=phone_number,email=email,address=address,password=make_password(password))
        messages.success(request, "Account created successfully!")
        return redirect('login')
    return render(request,'register.html')


def forgotPassword(request):
    return render(request, 'forgot-password.html')

def page_404(request):
    return render(request,'404.html')

def blank_page(request):
    return render(request,'blank.html')

def charts(request):
    return render(request,'charts.html')

def tables(request):
    return render(request,'tables.html')

