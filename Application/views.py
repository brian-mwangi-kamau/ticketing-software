from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('console')
    else:
        form = LoginForm
    return render(request, 'registration/login.html', {'form': form})



@login_required
def console(request):
    user = request.user
    if user.is_admin:
        return render(request, 'staff_console.html')
    else:
        return render(request, 'console.html')
    

    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')