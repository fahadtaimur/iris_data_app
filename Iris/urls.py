from django.urls import path, include
from .views import *
app_name = "iris"

urlpatterns = [
    path('table/', TableView, name="table"),
]