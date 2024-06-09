from django.shortcuts import get_object_or_404, render

from .models import Dataset

def index(request):
    datasets_list = Dataset.objects.order_by("title")
    context = { 'datasets_list': datasets_list, }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    selected_chart = dataset.chart_set.first()
    filter_value = request.GET.get('filter_value')

    if filter_value == None:
        first_filter_value = selected_chart.get_first_filter_value()
        filter_value = first_filter_value.astype(str)

    context = {
        "dataset": dataset,
        "chart": selected_chart.get_context(filter_value)
    }

    return render(request, 'datasets/detail.html', context)
