from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm, UserCreationForm, CustomAuthenticationForm
from django.http import HttpRequest, HttpResponse

# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    auth_form = UserCreationForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

    if auth_form.is_valid() and profile_form.is_valid():
        user = auth_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
    context = {
        'auth_form': auth_form,
        'profile_form': profile_form,
    }
    return render(request, "account/register.html", context)

def login_view(request: HttpRequest) -> HttpResponse:
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged In!')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect email or password!')
            return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, "account/login.html", context)


@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, "account/logout.html", {})