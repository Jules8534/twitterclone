from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("users/", views.allusers_view, name="all_users"),
    path("user/<str:slug>/follow_user", views.follow_user_view, name="follow_user"),
    path("user/<str:slug>/unfollow_user", views.unfollow_user_view, name="unfollow_user"),
    path("newuser/", views.newuser_view, name="newuser"),
    path("user/<str:slug>/", views.user_detail_view, name="user_detail"),
    
    
]
