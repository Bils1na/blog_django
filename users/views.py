from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import RegistrationForm, EditProfileForm


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
    error_message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            if "Passwords do not match." in str(form.errors):
                error_message = "Password do not match. Enter new password."
            elif "Email already exists." in str(form.errors):
                error_message = "Email already exists. You need to enter other email."
            elif "Username already exists." in str(form.errors):
                error_message = "Username already exists. You need to enter other username."
            
            return render(request, "registration/register.html", {"error": error_message})
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

<<<<<<< HEAD
# def edit_full_name(request):
#     if request.method == "POST":
        

=======
    
@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user_id == request.user.id:
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect("users:profile", user_id)
        else:
            form = EditProfileForm(instance=user)
        return render(request, "registration/edit_profile.html", {"form": form})
    else:
        raise Http404
>>>>>>> fedef2c92b2c58a4be05a1b9e569e1b7f00eba0b

@login_required
def profile(request, user_id):
    # User profile page
    user = get_object_or_404(User, id=user_id)
    if user_id == request.user.id:
        return render(request, 'registration/profile.html', {'user': user})
    else:
        raise Http404
