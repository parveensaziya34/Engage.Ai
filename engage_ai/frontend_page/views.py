from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
            username = email.split('@')[0]
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login_page')

    return render(request, 'signup.html')


# Dashboard page
@login_required
def dashboard_page(request):
    user = request.user
    profile_photo = ''
    if hasattr(user, 'profile') and user.profile.photo:
        profile_photo = user.profile.photo.url

    context = {
        'username': user.first_name or user.username,
        'profile_photo': profile_photo
    }
    return render(request, 'dashboard.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Access Matrix Page
@login_required
def access_page(request):
    default_avatar_url = '/static/avtar1.jpg'
    user = request.user

    user_name = user.get_full_name() or user.username
    user_email = user.email
    user_avatar_url = default_avatar_url

    # Update avatar URL from profile
    if hasattr(user, 'userprofile') and user.userprofile.photo:
        user_avatar_url = user.userprofile.get_avatar_url()

    # Prepare all users
    all_users = User.objects.all()
    user_data = []
    for u in all_users:
        name = u.get_full_name() or u.username
        email = u.email
        avatar = default_avatar_url
        if hasattr(u, 'userprofile') and u.userprofile.photo:
            avatar = u.userprofile.get_avatar_url()
        user_data.append({
            'name': name,
            'email': email,
            'avatar': avatar
        })

    context = {
        'user_name': user_name,
        'user_email': user_email,
        'user_avatar_url': user_avatar_url,
        'users_json': user_data  # used in JS
    }

    return render(request, 'access_matrix_admin.html', context)

# Chatbot page
@login_required
def chatbot_page(request):
    return render(request, 'chatbot.html')


# Logout function
def logout_user(request):
    logout(request)
    return redirect('login_page')


# Calendar page
@login_required
def calender_page(request):
    return render(request, 'calender.html')


# Contact Policy Admin page
@login_required
def control_page(request):
    return render(request, 'control_policy_admin.html')
