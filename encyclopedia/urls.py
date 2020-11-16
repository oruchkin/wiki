from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikititle, name="wikititle"),
    path("wiki/", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("new-page", views.newpage, name="new page"),
    path("save-page", views.save_page, name="save_page"),
    path("random-page", views.random_page, name="random page"),
    path("edit-page/<str:title>", views.edit_page, name="edit page"),
    
    ]
