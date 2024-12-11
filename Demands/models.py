from django.db import models
from Accounts.models import User

# Create your models here.

class Demand(models.Model):
    demander = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    To=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Demands'
        verbose_name = 'مطالبه'
        verbose_name_plural = 'مطالبات'
