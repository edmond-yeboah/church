from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customusers(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True)
    tel = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    admin = models.BooleanField(default=False)
    bio = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.username

