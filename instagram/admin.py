from django.contrib import admin
from .models import Profile, Post, Tag, Comment, Notification, Follow, Likes, Message

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Follow)
admin.site.register(Likes)
admin.site.register(Message)

