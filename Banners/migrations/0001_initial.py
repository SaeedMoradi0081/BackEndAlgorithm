# Generated by Django 5.1.4 on 2024-12-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'بنر',
                'verbose_name_plural': 'بنر ها',
                'db_table': 'banners',
            },
        ),
    ]
