from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
  username = models.CharField(max_length=80, unique=True, blank=True)
  identification_number = models.IntegerField(default=1)
  email_address = models.EmailField(blank=True)
  neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, null=True, blank=True)


  USERNAME_FIELD = 'username'

  def __str__(self):
    return self.username

  def save_user(self):
    self.save()

  def create_user(self,email_address, password=None):
    if not email_address:
      raise ValueError('missing email address')
    user = self.model(email_address=email_address)
    user.set_password(password)
    user.save(using=self._db)
    return user


class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True)
  bio = models.TextField(max_length=200, blank=True)
  image = CloudinaryField('image', blank=True)
  location = models.CharField(max_length=80, blank=True)


  def __str__(self):
    return self.user.username

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()


class Neighborhood(models.Model):
  name = models.CharField(max_length=80, blank=True)
  location = models.CharField(max_length=80, blank=True)
  population = models.IntegerField(blank=True)


  def __str__(self):
    return self.name


class Business(models.Model):
  name = models.CharField(max_length=100, blank=True)
  email_address = models.EmailField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True)
  neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE, blank=True)

  def __str__(self):
    return self.name


