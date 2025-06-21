from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Login view
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard_page')
            else:
                messages.error(request, "Invalid password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials. Please sign up.")
    
    return render(request, 'login_screen.html')

# Signup view
def signup_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            username = email.split('@')[0]  # Optional: use uuid for unique usernames
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login_page')

    return render(request, 'signup.html')

# Dashboard page
def dashboard_page(request):
    return render(request, 'dashboard.html')

# Access Matrix Admin page
def access_page(request):
    return render(request, 'access_matrix_admin.html')

# Chatbot page
def chatbot_page(request):
    return render(request, 'chatbot.html')

# Logout function
def logout_user(request):
    logout(request)
    return redirect('login_page')

# Calendar page
def calender_page(request):
    return render(request, 'calender.html')


def control_page(request):
        return render(request,'control_policy_admin.html',{})
