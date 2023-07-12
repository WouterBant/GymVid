from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Videos_Posted, Category, Comments, Profile, Subscribers
from . import util

import random


""" Functions that render pages, in some cases making use of information from the database. """


# Renders the main page
def index(request):
    videos = Videos_Posted.objects.all()
    categories = Category.objects.all()

    return render(request, "videos/index.html", {
        "videos": videos,
        "categories": categories
    })


# Renders the login page: Harvard template
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "videos/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "videos/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Renders the register page: Harvard template (most)
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "videos/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

            # Create new profile
            newProfile = Profile(
                person=user,
            )
            newProfile.save()

        except IntegrityError:
            return render(request, "videos/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "videos/register.html")


# Renders the leaderboard page
def leaderboard(request):
    videos = Videos_Posted.objects.order_by('-likes')

    return render(request, "videos/leaderboard.html", {
        "videos": videos
    })


# Renders the subscription page
def subscriptions(request):
    userNow = request.user
    creators = Subscribers.objects.filter(follower=userNow).values_list('creator', flat=True)

    # Select all the videos of the creators followed
    videos = Videos_Posted.objects.filter(creator__in=creators)

    return render(request, "videos/subscriptions.html", {
        "videos": videos
    })



# Renders the upload page
def upload(request):
    categories = Category.objects.all()

    return render(request, "videos/upload.html", {
        "categories": categories
    })


# Renders the profile page
def profile(request):
    userNow = request.user
    profileData = Profile.objects.get(person=userNow)
    videos = Videos_Posted.objects.filter(creator=userNow)
    subCount = Subscribers.objects.filter(creator=userNow).all().count()

    return render(request, "videos/profile.html", {
        "profile_info": profileData,
        "videos": videos,
        "number_of_subscribers": subCount
    })


# Renders the video page
def video(request, title):
    if request.method == "GET":
        # Get information about the video
        video = Videos_Posted.objects.get(title=title)
        saved = request.user in video.video_saved.all()
        liked = request.user in video.video_liked.all()
        allComments = Comments.objects.filter(comment_video=video).order_by('-likes')

        # See if the user is subscribed to the creator of the video
        userNow = request.user
        creator = video.creator
       
        subbed = Subscribers.objects.filter(creator=creator, follower=userNow).exists()

        return render(request, "videos/video.html", {
            'video': video,
            'saved': saved,
            'liked': liked,
            'allComments': allComments,
            'subbed': subbed
        })


# Shows the search results of the term(s) used in the searchbar
def search(request):
    search_term = request.POST['term'].lower()
    videos = Videos_Posted.objects.filter(title__icontains=search_term)

    return render(request, "videos/search.html", {
        "videos": videos
    })


# Makes it possible to filter the videos on the main page
def display_category(request):
    selected_category = request.POST['category']
    category_object = Category.objects.get(category=selected_category)
    list_of_videos = Videos_Posted.objects.filter(category_video=category_object)

    return render(request, "videos/index.html", {
        "videos": list_of_videos,
        "categories": Category.objects.all()
    })


# Makes it possible to go to the profile page of another user
def go_to_profile(request, id):
    # Get the creator of the video
    record = Videos_Posted.objects.select_related('creator').get(id=id)
    creator = record.creator

    # Get all videos of the creator
    videos = Videos_Posted.objects.filter(creator=creator)

    # Get description and profile name of creator
    profileData = creator.person.all().get()

    # Get the title of one of the videos, this is needed for subscribing
    title = videos.values('title').first()

    # Get the count of subscribers
    subCount = Subscribers.objects.filter(creator=creator).count()

    # Check if the current user follows the creator
    userNow = request.user
    subbed = Subscribers.objects.filter(creator=creator, follower=userNow).exists()

    return render(request, "videos/go_to_profile.html", {
        "creator": creator,
        "videos": videos,
        "profile_information": profileData,
        "title": title['title'] if title else None,
        "number_of_subs": subCount,
        "user": userNow,
        "subbed": subbed
    })


# Renders the page which shows all saved videos
def saved(request):
    userNow = request.user
    savedVideos = userNow.video_saved.all()

    return render(request, "videos/saved.html", {
        "videos": savedVideos
    })


# Renders the page on which you can generate the personal scheme
def get_scheme(request, id):
    return render(request, "videos/scheme.html", {
        "video": Videos_Posted.objects.get(id=id),
        "scheme": None
    })


""" Functions that add records to the database. """


# Makes it possible to add comments to videos
def addComment(request, id):
    # Get the data needed for the new Comments record
    userNow = request.user
    video = Videos_Posted.objects.get(pk=id)
    title = video.title
    message = request.POST['newComment']

    # Make a new Comments record
    newComment = Comments(
        author=userNow,
        comment_video=video,
        message=message
    )
    newComment.save()

    return HttpResponseRedirect(reverse("video", args=(title, )))


# Makes it possible to subscribe to a creator from the video page
def addSub(request, title):
    # Get the creator of the video and the current user
    record = Videos_Posted.objects.get(title=title)
    creator = record.creator
    userNow = request.user

    # Make a new record in the Subscribers model
    newSub = Subscribers(
        follower=userNow,
        creator=creator
    )
    newSub.save()

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to upload videos
def upload_video(request):
    # Get the data from the form
    title = request.POST['title']
    description = request.POST['description']
    video = request.FILES['video']
    thumbnail = request.FILES['thumbnail']
    scheme = request.FILES['scheme'] if 'scheme' in request.FILES else False
    no_scheme = False if scheme else True
    category = Category.objects.get(category=request.POST['category'])
    creator = request.user

    # Make a new record for the Videos_Posted model
    new_video = Videos_Posted(
        title=title,
        description=description,
        video_file=video,
        thumbnail=thumbnail,
        training_scheme=scheme,
        no_training_scheme=no_scheme,
        category_video=category,
        creator=creator
    )
    new_video.save()

    return HttpResponseRedirect(reverse(index))


""" Functions that delete records from the database. """


# Handles deleting the video
def delete_video(request, id):
    Videos_Posted.objects.get(pk=id).delete()

    return HttpResponseRedirect(reverse(index))


# Makes it possible to unsubscribe to a creator
def removeSub(request, title):
    # Get the creator
    record = Videos_Posted.objects.get(title=title)
    creator = record.creator

    # Remove the record where the user follows the creator of the video
    userNow = request.user
    data = Subscribers.objects.get(follower=userNow, creator=creator)
    data.delete()

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to remove your posted comment
def removeComment(request, pk):
    # Remove the comment
    comment = Comments.objects.get(pk=pk)
    Comments.objects.get(pk=pk).delete()

    # Get the title of the video for redirecting
    title = comment.comment_video.title

    return HttpResponseRedirect(reverse("video", args=(title,)))


""" Functions that update information in the database. """


# Handles the updating of username and description of a user
def update_information(request, id):
    data = Profile.objects.get(pk=id)
    data.profile_name = request.POST['new_username']
    data.profile_description = request.POST['new_description']
    data.save()

    return HttpResponseRedirect(reverse(index))


# Handles deleting videos from saved, from saved page
def delete_from_saved(request, title):
    data = Videos_Posted.objects.get(title=title)
    userNow = request.user
    data.video_saved.remove(userNow)

    return HttpResponseRedirect(reverse("saved"))


# Handles deleting videos from saved, from video page
def removeSaved(request, title):
    data = Videos_Posted.objects.get(title=title)
    userNow = request.user
    data.video_saved.remove(userNow)

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Handles adding videos to saved
def addSaved(request, title):
    data = Videos_Posted.objects.get(title=title)
    userNow = request.user
    data.video_saved.add(userNow)

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to like videos
def addLike(request, title):
    video = Videos_Posted.objects.get(title=title)

    # Add the user the the group of people who liked this video
    userNow = request.user
    video.video_liked.add(userNow)

    # Update number of likes
    video.likes += 1
    video.save(update_fields=["likes"])

    # Get the title of the video for redirecting
    title = video.title

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to remove likes on videos
def removeLike(request, title):
    video = Videos_Posted.objects.get(title=title)

    # Remove the user the the group of people who liked this video
    userNow = request.user
    video.video_liked.remove(userNow)

    # Update number of likes
    video.likes -= 1
    video.save(update_fields=["likes"])

    # Get the title of the video for redirecting
    title = video.title

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to like comments
def addLikeComment(request, pk):
    # Get the user and the comment
    userNow = request.user
    comment = Comments.objects.get(pk=pk)

    # Add the user to the group of people who like the comment
    comment.comment_liked.add(userNow)

    # Update the number of likes for the comment
    comment.likes += 1
    comment.save(update_fields=["likes"])

    # Get the title for redirecting
    title = comment.comment_video.title

    return HttpResponseRedirect(reverse("video", args=(title,)))


# Makes it possible to remove the like for your comment
def removeLikeComment(request, pk):
    # Get the user and comment
    userNow = request.user
    comment = Comments.objects.get(pk=pk)

    # Remove the user from the group of people who liked the comment
    comment.comment_liked.remove(userNow)

    # Update the number of likes for the comment
    comment.likes -= 1
    comment.save(update_fields=["likes"])

    # Get the title of the video for redirecting
    title = comment.comment_video.title

    return HttpResponseRedirect(reverse("video", args=(title,)))


""" Function that generates personal schemes making use of the functions in util.py. """


# Makes it possible to generate the personal scheme
def download_scheme(request, id):
    # Get information needed to generate the scheme
    video = Videos_Posted.objects.get(pk=id)
    creator = video.creator
    subject = video.title
    userNow = request.user

    # Get the location of the excel file posted by the creator
    df = video.training_scheme

    # Get the max weight from form
    max_one_rep = int(request.POST["max_weight"])

    # Make a hash to generate unique file names
    hash = random.getrandbits(32)

    # Make the file and store it in external directory which stores media files
    util.make_personal_scheme(df, userNow, creator, subject, max_one_rep, hash)

    # Determine the filename which the scheme has in the directory
    filename = f"{subject}_{userNow}_{hash}.pdf"

    return render(request, "videos/scheme.html", {
        "video": video,
        "scheme": filename,
    })
