# Generated by Django 5.1.4 on 2024-12-11 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_user_picture'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]