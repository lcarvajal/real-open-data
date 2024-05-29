from django.shortcuts import get_object_or_404, render
from django.conf import settings

import json
from .models import Dataset
import os
import pandas as pd

def index(request):
    datasets_list = Dataset.objects.order_by("title")
    context = { 'datasets_list': datasets_list, }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)

    # Get query parameters
    file_path = os.path.join(settings.STATIC_ROOT, dataset.file_path)
    df = pd.read_csv(file_path)
    x_column = request.GET.get('x')
    y_column = df.columns[2]
    filter_column = request.GET.get('filter')
    current_filter_option = int(request.GET.get('filter_value'))

    print(df[filter_column].unique())
    print(current_filter_option)

    # JSON data for chart generation
    filtered_df = df[df[filter_column] == current_filter_option]
    labels = filtered_df[x_column].tolist()
    data = filtered_df[y_column].tolist()
    chart_data = {
        'labels': labels,
        'datasets': [{
            'label': 'Dataset Label',  # You can customize this label
            'data': data
        }]
    }
    json_data = json.dumps(chart_data)

    context = {
        'dataset': dataset,
        'filter_title': filter_column,
        'filter_options': df[filter_column].unique(),
        'current_filter_option': current_filter_option,
        'json_data': json_data
    }

    return render(request, 'datasets/detail.html', context)

def analysis(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    return render(request, 'datasets/analysis.html', { 'dataset': dataset })