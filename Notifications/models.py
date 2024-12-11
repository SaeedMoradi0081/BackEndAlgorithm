from django.db import models

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Notifications'
        verbose_name_plural = 'اطلاع رسانی ها'
        verbose_name = 'اطلاع رسانی'
