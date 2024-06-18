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
    selected_chart = dataset.chart_set.first()
    filter_value = request.GET.get('filter_value')

    if filter_value is None:
        first_filter_value = selected_chart.get_first_filter_value()
        filter_value = first_filter_value.astype(str)

    return Response({
        "dataset": dataset,
        "chart": selected_chart.get_context(filter_value)
    })