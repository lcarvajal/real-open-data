from django.contrib import admin
from .models import Dataset, Chart, ChartType

admin.site.register(Dataset)
admin.site.register(Chart)
admin.site.register(ChartType)
