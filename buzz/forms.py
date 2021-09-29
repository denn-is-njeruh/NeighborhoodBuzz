from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,User
from django.contrib.auth import get_user_model

User = get_user_model()

#Your form details here


class NewUserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ("username", "email", "password1","password2")

  def save(self,commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user


class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('image','user','bio','location')