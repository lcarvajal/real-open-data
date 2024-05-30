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
    
class ChartType(models.Model):
    name = models.CharField(max_length=80)

class Chart(models.Model):
    x_column = models.CharField(max_length=80)
    y_column = models.CharField(max_length=80)
    filter_column = models.CharField(max_length=80)

    chart_type = models.ForeignKey(ChartType, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)