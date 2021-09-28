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

  def save(self):
    return self.save()

  def delete(self):
    return self.delete()
