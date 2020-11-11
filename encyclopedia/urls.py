from django.urls import path

from . import views

app_name = "ecylcopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikititle,name="wikititle"),
    path("wiki/", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
]
