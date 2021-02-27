from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_entry, name="get_entry"),
    path("wiki/<str:task>", views.search_field, name="search_field")
]