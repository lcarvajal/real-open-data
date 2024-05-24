from django.db import models

# Create your models here.

# Run `python manage.py makemigrations` after making changes
# Then run `python manage.py migrate`

class Dataset(models.Model):
    name = models.CharField(max_length=80)
    file_path = models.CharField(max_length=80)