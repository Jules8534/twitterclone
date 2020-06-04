from django.urls import path

from . import views

urlpatterns = [
    path("notification/", views.notifications, name="notifications"),
]