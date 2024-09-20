from django.urls import path

from . import views

app_name = "tailwindApp"
urlpatterns = [
    path("", views.index, name="index"),
]