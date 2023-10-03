from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import RegistrationForm


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("blog:index")
        else:
            return render(request, "registration/login.html", {"error": "Invalid account"})

    return render(request, "registration/login.html")


def log_out(request):
    # Log out
    logout(request)
    return render(request, "registration/logged_out.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
           return render(request, "registration/register.html", {"error": "Email exists"}) 
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# def change_full_name(request):
#     if request.method == "POST":
#         new_first_name = request.POST["first_name"]
#         new_last_name = request.POST["last_name"]


@login_required
def profile(request, user_id):
    # User profile page
    user = get_object_or_404(User, id=user_id)
    if user_id == request.user.id:
        return render(request, 'registration/profile.html', {'user': user})
    else:
        raise Http404
