from django.urls import path

from . import views

url_patterns = [
    path("", views.index)
    path("results/<str>", views.results)
]
