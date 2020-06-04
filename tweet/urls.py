from django.urls import path
from . import views



urlpatterns = [
   path("new_tweet/", views.new_tweet, name="new_tweet"),
   path("all_tweets_view/", views.all_tweets_view, name="all_tweets_view"),
   path("tweet/<int:pk>", views.tweet, name="tweet"), 
]

