from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html',)

def register_user(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, f'Registration Successful.')
      return redirect('homepage')
    messages.error(request, f'Unsuccessful registration. Invalid information.')
  form = NewUserForm()
  return render(request, 'registration/registration_form.html', {"registration_form": form})