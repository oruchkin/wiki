from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikititle, name="wikititle"),
    path("wiki/", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
<<<<<<< HEAD
    path("new-page", views.newpage, name="new page"),
    path("save-page", views.save_page, name="save_page"),
    ]
=======
]
>>>>>>> parent of 77ae1c9... 41
