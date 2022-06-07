from django.test import TestCase
from .models import *

class CommentTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='shiru')

        self.comment= Comment.objects.create(poster= self.user, comment='looking good' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)

