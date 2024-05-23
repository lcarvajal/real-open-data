from django.db import models

# Create your models here.

# Run `python manage.py makemigrations` after making changes

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()