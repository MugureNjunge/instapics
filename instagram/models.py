from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.urls import reverse
from django.db.models.signals import post_save
import uuid
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_picture", null=True, default="default.jpg")
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def create_user_profile(sender, instance, created, **kwargs):
      if created:
        Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)

class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    squareImage = models.ImageField(upload_to="new_post", null=True, default="default.jpg")
    caption = models.CharField(max_length=10000, verbose_name="Caption")
    posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)



     
