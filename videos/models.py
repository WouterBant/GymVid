from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Videos_Posted(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    premium = models.BooleanField(default=False)
    thumbnail = models.ImageField()
    video_file = models.FileField()
    training_scheme = models.FileField(blank=True, null=True)
    no_training_scheme = models.BooleanField(default=True)
    category_video = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_video", default=None)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    video_saved = models.ManyToManyField(User, related_name="video_saved", blank=True)
    video_liked = models.ManyToManyField(User, related_name="video_liked", blank=True)
    time_posted = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    comment_video = models.ForeignKey(Videos_Posted, on_delete=models.CASCADE, related_name="comment_video")
    message = models.CharField(max_length=500)
    comment_liked = models.ManyToManyField(User, related_name="comment_liked", blank=True)
    likes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} comment on {self.comment_video}"


class Profile(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")
    profile_name = models.CharField(max_length=20, default="No profile name")
    profile_description = models.CharField(max_length=500, default="No description")
    videos = models.ManyToManyField(Videos_Posted, related_name="videos", blank=True)

    def __str__(self):
        return f"{self.profile_name} has description {self.profile_description}"


class Subscribers(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subfollower")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcreator")

    def __str__(self):
        return f"{self.follower} follows {self.creator}"
