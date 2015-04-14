from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class CustomUser(User):
    description = models.TextField(max_length=256, default="",blank=True)
    scope = models.IntegerField(default=100)
    
    objects = UserManager()