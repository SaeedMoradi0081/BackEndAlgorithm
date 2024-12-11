from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.

class User(AbstractUser):
    nationality_code = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)
    picture = models.CharField(max_length=255,default='')


    def __str__(self):
        return self.username
    class Meta:
        db_table = 'users'
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'