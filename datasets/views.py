from django.shortcuts import get_object_or_404, render

from .models import Dataset, Chart

def index(request):
    datasets_list = Dataset.objects.order_by("title")
    context = { 'datasets_list': datasets_list, }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    selected_chart = dataset.chart_set.first()
    filter_value = request.GET.get('filter_value')

    context = {
        "dataset": dataset,
        "chart": selected_chart.get_context(filter_value)
    }

    return render(request, 'datasets/detail.html', context)
