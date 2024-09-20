from django.urls import path

from . import views

app_name = "backtesting"
urlpatterns = [
    path("", views.index, name="index"),
    path("charts/<int:tradable_id>/", views.chart, name="charts"),
    path("coinflip", views.coinflip, name="coinflip"),
]