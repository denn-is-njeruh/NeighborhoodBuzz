from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,User

class NewUserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ("username", "email_address", "password1","password2")

  def save(self,commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email_address = self.cleaned_data['email_address']
    if commit:
      user.save()
    return user


class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email_address']


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('image','user','bio','location')