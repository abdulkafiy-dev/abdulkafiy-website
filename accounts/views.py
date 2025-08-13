from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods

# Checking for if username / password is invalid
def check_credentials(username, password):
    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return False
    except User.DoesNotExist:
        return False
    return True

# Login View 
def log_in(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/login.html', messages.error(request, "You've logged in already!"))
        # return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if not check_credentials(username, password):
            return render (request, 'accounts/login.html', messages.error(request, 'Please enter the correct username and password for this account. Note that both fields may be case-sensitive. '))

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('index')
    else:
        return render(request, 'accounts/login.html')

# Logout View
def log_out(request):
    logout(request)
    return redirect('/accounts/')