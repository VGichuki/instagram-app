from django.test import TestCase
from .models import Profile,Post,Comment
from django.contrib.auth.models import User
# Create your tests here.

class PostTestCase(TestCase):
    '''
    class that tests the posts class
    '''
    def setUp(self):
        self.wangari = User(user='wangari')
        self.wangari.save()

    # def test_save_post(self):
    #     self.pokemon.save_post()
    #     posts = Post.objects.all()
    #     self.assertEquals(len(posts),1)

    

