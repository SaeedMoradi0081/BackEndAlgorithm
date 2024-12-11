from django.db import models

from Accounts.models import User


# Create your models here.
class Participation(models.Model):
    participationer=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    goal=models.CharField(max_length=100)
    start_at=models.CharField(max_length=100)
    time=models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table='participations'
        verbose_name = 'مشارکت'
        verbose_name_plural = 'مشارکت ها'

