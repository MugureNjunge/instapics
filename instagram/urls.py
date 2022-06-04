from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('',views.home, name='home'),
  path('', views.EditProfile, name="editprofile"),

  path('sign-up/', views.register, name="sign-up"),
  path('sign-in/', views.LogIn, name='sign-in'),
  # path('sign-out/', views.Logout,  name='sign-out'),

  # path('sign-in/', views.LogIn, redirect_authenticated_user=True, name='sign-in'),
  # path('category/<int:category_id>/',views.categoryPage , name='image-category'),
  # path('location/<int:location_id>/',views.locationPage , name='image-location'),
 
  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


