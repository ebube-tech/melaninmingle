from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Create your views here.

def login_view(request):
    pass


@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, "accounts/logout.html", {})