from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'banners'
        verbose_name_plural = 'بنر ها'
        verbose_name = 'بنر'
