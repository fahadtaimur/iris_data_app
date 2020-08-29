from django.urls import path, include
from .views import data_import_view

app_name = "csvs"
urlpatterns = [
    path('', data_import_view, name='csv'),
]