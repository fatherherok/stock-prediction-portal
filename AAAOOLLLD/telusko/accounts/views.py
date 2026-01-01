# yourapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")  # or use a named URL: redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please check your username and password.")
            return redirect('login')
    else:
        return render(request, 'login.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '').strip().lower()

        # Basic required-field validation
        if not username or not password1 or not password2 or not email:
            messages.error(request, "Please fill in all required fields.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username__iexact=username).exists():
            messages.info(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email__iexact=email).exists():
            messages.info(request, "Email already registered.")
            return redirect('register')

        # Optional: enforce minimum password length
        if len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect('register')

        # create user (password will be hashed)
        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        # create_user already saves the user
        messages.success(request, "User created successfully! You can now log in.")
        return redirect('login')

    # GET or other -> render registration form
    return render(request, 'register.html')




def logout(request):
   auth.logout(request)
   return return redirect('/')