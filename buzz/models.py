from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
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

