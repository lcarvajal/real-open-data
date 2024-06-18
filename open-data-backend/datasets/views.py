from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DatasetSerializer

from .models import Dataset

@api_view(['GET'])
def index(request):
    datasets = Dataset.objects.order_by("title")
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    serializer = DatasetSerializer(dataset, many=False)
    selected_chart = dataset.chart_set.first()
    filter_value = request.GET.get('filter_value')

    if filter_value is None:
        first_filter_value = selected_chart.get_first_filter_value()
        filter_value = first_filter_value.astype(str)

    chart_context = selected_chart.get_context(filter_value)

    chart_options = {
                'maintainAspectRatio': False,
                'legend': {
                    'display': False
                },
                'scales': {
                    'x': {
                        'display': True,
                        'title': {
                        'display': True,
                        'text': chart_context['y_title'],
                        'padding': { 'top': 20, 'left': 0, 'right': 0, 'bottom': 0 },
                        }
                    },
                    'y': {
                        'display': True,
                        'title': {
                        'display': True,
                        'text': chart_context['x_title'],
                        'padding': { 'top': 30, 'left': 0, 'right': 0, 'bottom': 0 },
                        }
                    }
                }
            }
    chart_data = {
                'labels': chart_context['x_labels'],
                'datasets': [{
                    'data': chart_context['y_values']
                }]
            }

    return Response({
        "dataset": serializer.data,
        "chart": chart_context,
        "chart_options": chart_options,
        "chart_data": chart_data
    })