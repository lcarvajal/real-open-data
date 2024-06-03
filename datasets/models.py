from django.db import models
from django.conf import settings

import os
import pandas as pd

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
    
    def get_data_frame(self):
        file_path = os.path.join(settings.STATIC_ROOT, self.file_path)
        return pd.read_csv(file_path)
    
class ChartType(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Chart(models.Model):
    title = models.CharField(max_length=80, default='')
    x_column = models.CharField(max_length=80)
    y_column = models.CharField(max_length=80)
    filter_column = models.CharField(max_length=80)

    chart_type = models.ForeignKey(ChartType, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)

    def __str__(self):
        return self.dataset.title
    
    def get_context(self, filter_value):
        chart_df = self.dataset.get_data_frame()

        if filter_value:
            filtered_chart_df = chart_df[chart_df[self.filter_column] == int(filter_value)]
            labels = filtered_chart_df[self.x_column].tolist()
            data = filtered_chart_df[self.y_column].tolist()
        else:
            labels = chart_df[self.x_column].tolist()
            data = chart_df[self.y_column].tolist()
        
        chart_data = {
            "labels": labels,
            "datasets": [{
                "data": data
            }]
        }

        context = {
            "filter_value": filter_value,
            "filter_title": self.filter_column.replace("_", " ").lower(),
            "filter_options": chart_df[self.filter_column].unique().astype(str).tolist(),
            "x_title": self.x_column.replace("_", " ").lower(),
            "y_title": self.y_column.replace("_", " ").lower(),
            "json_data": chart_data,
            "type": self.chart_type.name,
        }

        return context
