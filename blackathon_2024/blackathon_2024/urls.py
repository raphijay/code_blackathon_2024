from django.urls import path, re_path
from blackathon_2024 import views

urlpatterns = [
    path("/Perspective/<int:id>/Endorse/", views.endorse),
]