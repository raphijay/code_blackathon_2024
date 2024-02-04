from django.urls import path, re_path
from blackathon_2024 import views

urlpatterns = [
    path("Tag/", views.addtag),
    path("Perspective/<int:id>/Endorse/", views.endorse),
    path("Perspective/<int:id>/Oppose/", views.oppose),
    path("Perspective/", views.addperspective),
    path("Perspective/<int:id>/", views.perspective_choice),
    path("Perspectives/", views.getperspectives_all),
    path("Event/", views.addevent),
    path("Event/<int:id>/", views.event_choice),
    path("Events/", views.getevents_all),
]