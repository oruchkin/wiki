from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("wiki/<str:wikititle>", views.wikititle, name="wikititle"),
]
