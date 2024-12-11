from django.db import models
from Accounts.models import User

# Create your models here.


class Cas(models.Model):
    caser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    To = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cas'
        verbose_name = 'انتقادات و پیشنهادات'
        verbose_name_plural = 'انتقادات و پیشنهادات'
