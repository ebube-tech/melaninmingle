from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, UserCreationForm
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
    
    return render(request, "account/login.html", {})


@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, "account/logout.html", {})