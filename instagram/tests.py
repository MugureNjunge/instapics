from django.test import TestCase
from .models import *


class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='shiru')
        self.profile = Profile.objects.create(user = self.user,bio = 'boogie with me')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('shiru')
        self.assertTrue(len(profile) > 0)
