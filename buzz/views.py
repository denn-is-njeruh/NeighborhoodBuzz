from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserForm,ProfileForm,UpdateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, 'index.html',)

def register_user(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, 'Registration Successful.')
      return redirect('homepage')
    messages.error(request, 'Unsuccessful registration. Invalid information.')
  form = NewUserForm()
  return render(request, 'registration/registration_form.html', {"registration_form": form})


def login_user(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
        login(request, user)
        messages.info(request, "You are now logged in as {username}.")
        return redirect('homepage')
      else:
        messages.error(request, 'Invalid Username or password')
    else:
      messages.error(request, 'Invalid username or password')
  form = AuthenticationForm()
  return render(request, 'registration/login_form.html', {"login_form": form})


def logout_user(request):
  logout(request)
  messages.info(request, 'You have successfully logged out.')
  return redirect('login')


@login_required
def profile(request):
  if request.method == 'POST':
    user_form = UpdateUserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Your profile was successfully updated!')
      return redirect('profileupdate')
    else:
      messages.error(request,'Please try updating your profile again.')
  else:
    user_form = UpdateUserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return render(request,'profile/profile.html',{"user_form": user_form, "prolife_form":profile_form})