from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm
from .models import UserProfile

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user_profile = request.user.profile
            location = user_profile.location
            age = user_profile.age
        except UserProfile.DoesNotExist:
            location = 'N/A'
            age = 'N/A'
    else:
        username = 'not logged in'
        location = 'N/A'
        age = 'N/A'

    context = {
        'username': username,
        'location': location,
        'age': age
    }
    return render(request, 'myapps/index.html', context)

@login_required
def profile(request):
    return render(request, 'myapps/profile.html')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'myapps/register.html', context)




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapps/login.html', {'form': form})