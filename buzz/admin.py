from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile,User,Neighborhood,Business

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Business)
