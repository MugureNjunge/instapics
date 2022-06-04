from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('profile/edit', views.EditProfile, name="editprofile"),

  path('sign-up/', views.register, name="sign-up"),
  path('sign-in/', views.LoginView(name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
  path('sign-out/', views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'),

  # path('category/<int:category_id>/',views.categoryPage , name='image-category'),
  # path('location/<int:location_id>/',views.locationPage , name='image-location'),
 
  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


