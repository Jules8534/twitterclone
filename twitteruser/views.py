from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth import login
from twitteruser.forms import NewTwitterUser
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

# Thanks for the help codementor.io!

def index(request):
    if request.user.is_authenticated:
        html = "index.html"
        tweets = Tweet.objects.filter(
            author__in=request.user.following.all()).order_by(
                "-creation_date")
        
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
        print(tweets)
        return render(request, html, {
            "tweets" : tweets, 
            "notifications": notifications
        })
    return redirect("/login/")

def allusers_view(request):
    html = "allusers_view.html"
    users = TwitterUser.objects.all()
    notifications = []
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
    print(users)
    return render(request, html, {
        'users': users,
        'notifications': notifications
    })

def newuser_view(request):
    if request.method == "POST":
        form = NewTwitterUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            new_user = TwitterUser.objects.last()
            new_user.set_password(raw_password=data['password'])
            new_user.following.add(new_user)
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))
    form = NewTwitterUser()
    return render(request, 'newuser_view_form.html', {"form": form})

def user_detail_view(request, slug):

        # model = Post
        # template_name = 'user_detail_view.html'
        # context_object_name = 'post'

    html = "user_detail_view.html"
    viewed_user = TwitterUser.objects.get(slug=slug)
    followers = TwitterUser.objects.filter(following=viewed_user)
    following = False
    user_tweets = Tweet.objects.filter(author=viewed_user).order_by(
        "-creation_date")
    notifications = []
    if request.user.is_authenticated:
        if viewed_user in request.user.following.all():
            following = True
        notifications = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
    return render(request, html, {
        'viewed_user': viewed_user,
        'following': following,
        'followers': followers,
        'user_tweets': user_tweets,
        'notifications': notifications
        })

def follow_user_view(request, slug):
    if request.user.is_authenticated:
        my_user = TwitterUser.objects.get(username=request.user.username)
        viewed_user = TwitterUser.objects.get(slug=slug)
        my_user.following.add(viewed_user)
        my_user.save()
    return redirect("/user/" + slug)


def unfollow_user_view(request, slug):
    if request.user.is_authenticated:
        my_user = TwitterUser.objects.get(username=request.user.username)
        viewed_user = TwitterUser.objects.get(slug=slug)
        my_user.following.remove(viewed_user)
        my_user.save()
    return redirect("/user/" + slug)

        