from django.urls import path, include
from .views import *
app_name = "iris"

urlpatterns = [
    path('table/', TableView, name="table"),
    path('scatterplot/', ScatterPlotView.as_view(), name='scatter'),
    path('scatterplot3d/', Scatter3DPlotView.as_view(), name='scatter3d'),
    path('histogram/', HistogramView.as_view(), name='histogram'),
    path('boxplot/', BoxPlotView.as_view(), name='boxplot'),
    path('density/', DensityContourView.as_view(), name='density'),
]