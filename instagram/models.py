from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True, blank=True, default=None)
    bio = models.TextField(blank=True,null=True ,default=None)
    profileimg = models.ImageField(upload_to='profile_images', default=None)
    location = models.CharField(max_length=100, blank=True, default=None)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='post_images', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100, default=None)
    user = models.CharField(max_length=100)
   

    def __str__(self):
        return self.user