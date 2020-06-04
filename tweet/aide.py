from notification.models import Notification
from twitteruser.models import TwitterUser
import re


def create_notifications(tweet):
    if "@" in tweet.tweet:
        users = find_mentioned_users(tweet.tweet)
        for user in users:
            if user in [x.username for x in TwitterUser.objects.all()]:
                Notification.objects.create(
                    tweet=tweet,
                    notified_user=TwitterUser.objects.get(username=user),
                    viewed=False
                )
    pass

def find_mentioned_users(tweet):
    mentioned_users = re.findall(r"@(\w+)\b", tweet)
    return mentioned_users
