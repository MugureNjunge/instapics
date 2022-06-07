from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from instagram.views import EditProfile

urlpatterns = [
    
    path('sign-up/',views.register,name='sign-up'),
    path('accounts/sign-in/',views.signin,name='sign-in'),
    path('sign-out/', views.signout, name='sign-out'),
     path('profile/edit', EditProfile, name="editprofile"),

]
