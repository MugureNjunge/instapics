from django.test import TestCase
from .models import *
from instagram.models import Profile

class PostTestClass(TestCase):
  
    def setUp(self):
        self.user = User.objects.create(id = 1, username='shiru')
        self.profile = Profile.objects.create(user = self.user,bio = 'forever young')

        self.image = Post.objects.create(name = self.user,profile = self.profile,caption ='lets be forever young',likes = 0,posted='7/06/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.picture,Post))

    def test_get_pictures(self):
        self.image.save()
        picture = Post.get_pictures()
        self.assertTrue(len(picture) == 1)


