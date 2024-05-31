from django.shortcuts import get_object_or_404, render
from django.conf import settings

import json
from .models import Dataset, Chart
import os
import pandas as pd

def index(request):
    datasets_list = Dataset.objects.order_by("title")
    context = { 'datasets_list': datasets_list, }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    charts = dataset.chart_set.all()
    selected_chart = charts[0]

    file_path = os.path.join(settings.STATIC_ROOT, dataset.file_path)
    df = pd.read_csv(file_path)

    # JSON data for chart generation
    current_filter_option = request.GET.get('filter_value')
    if current_filter_option is None:
        current_filter_option = 91700

    current_filter_option = int(current_filter_option)
    filtered_df = df[df[selected_chart.filter_column] == current_filter_option]
    labels = filtered_df[selected_chart.x_column].tolist()
    data = filtered_df[selected_chart.y_column].tolist()
    chart_data = {
        'labels': labels,
        'datasets': [{
            'data': data
        }]
    }
    json_data = json.dumps(chart_data)

    context = {
        'dataset': dataset,
        'filter_title': selected_chart.filter_column.replace("_", " ").lower(),
        'filter_options': df[selected_chart.filter_column].unique(),
        'x_title': selected_chart.x_column.replace("_", " ").lower(),
        'y_title': selected_chart.y_column.replace("_", " ").lower(),
        'current_filter_option': current_filter_option,
        'json_data': json_data
    }

    return render(request, 'datasets/detail.html', context)

def analysis(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    return render(request, 'datasets/analysis.html', { 'dataset': dataset })