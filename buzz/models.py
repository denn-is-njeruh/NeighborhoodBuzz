from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from cloudinary.models import CloudinaryField
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager



# Create your models here.
class UserManager(BaseUserManager):
  def create_user(self,username, password=None):
    if not username:
      raise ValueError('User must have a valid username')
    user = self.model(username=self.get_by_natural_key(username))
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_staffuser(self,username,password):
    user = self.creat_user(username,password=password)
    user.is_staff = True
    user.save(using=self.db)
    return user

  def create_superuser(self,username,password=None):
    user = self.create_user(username,password=password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self.db)
    return user

class User(AbstractBaseUser):
  username = models.CharField(max_length=80, unique=True, blank=True)
  identification_number = models.IntegerField(default=1)
  email = models.EmailField(verbose_name='email address', blank=True)
  neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE, null=True, blank=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.username

  def get_full_name(self):
    return self.username

  def get_username(self):
    return self.username

  def has_perm(self,perm,obj=None):
    return True

  @property
  def is_staff(self):
    return self.is_staff

  @property
  def is_superuser(self):
    return self.is_superuser

  objects = UserManager()


class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True)
  bio = models.TextField(max_length=200, blank=True)
  image = CloudinaryField('image', blank=True)
  location = models.CharField(max_length=80, blank=True)

  def __str__(self):
    return str(self.user.username)

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


