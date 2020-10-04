from django.urls import path

from . import views

urlpatterns = [
    path("form/", views.index),
    path("res/<int:id>", views.results),
    path("islem/", views.redirect)
]
