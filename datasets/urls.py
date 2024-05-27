from django.urls import path

from . import views

app_name = "datasets"
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /datasets/5/
    path("<int:dataset_id>/", views.detail, name="detail"),
    # ex: /datasets/5/analysis/
    path("<int:dataset_id>/analysis/", views.analysis, name="analysis"),
]