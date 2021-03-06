from django.db import models
from twitteruser.models import TwitterUser
# Create your models here.

class Tweet(models.Model):
    tweet = models.CharField(max_length=140,)


    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE,
        related_name="user_auther"
        )

    creation_date = models.DateTimeField()


    def __str__(self):
        return self.tweet
