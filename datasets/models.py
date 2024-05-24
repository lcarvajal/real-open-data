from django.db import models

# Create your models here.

# Check if there are problems with ` python manage.py check`
# Run `python manage.py makemigrations` after making changes
# Then run `python manage.py migrate`

class Dataset(models.Model):
    title = models.CharField(max_length=80)
    file_path = models.CharField(max_length=80)

    # Displays the title when the dataset is displayed in the console or admin
    def __str__(self):
        return self.title