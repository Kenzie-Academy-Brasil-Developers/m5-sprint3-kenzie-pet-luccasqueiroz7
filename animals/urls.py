from django.urls import path

from . import views

# Importar views...

urlpatterns = [
    path(
        "animals/",
        views.AnimalView.as_view(),
    ),
    path(
        "animals/<int:animal_id>/",
        views.AnimalDetailView.as_view(),
    ),
]
