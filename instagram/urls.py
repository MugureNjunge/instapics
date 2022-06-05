from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('', views.EditProfile, name="editprofile"),
  path('', views.EditProfile, name="rofile"),

  path('sign-up/', views.register, name="sign-up"),
  path('sign-in/', views.LogIn, name='sign-in'),
  # path('sign-out/', views.Logout,  name='sign-out'),
 
  path('', views.inbox, name="message"),
  path('direct/<username>', views.Directs, name="directs"),
  path('send/', views.SendDirect, name="send-directs"),
  path('search/', views.UserSearch, name="search-users"),
  path('new/<username>', views.NewConversation, name="conversation"), 
]

  # path('', models.Notification, name='show-notification'),



#   path('newpost', models.NewPost, name='newpost'),
#   path('<uuid:post_id>', models.PostDetail, name='post-details'),
#   path('tag/<slug:tag_slug>', models.Tag, name='tags'),
#   path('<uuid:post_id>/like', models.likes, name='like'),
# ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


