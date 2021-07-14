from datetime import date
from unittest import result
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

        self.pokemon = Post(image='pokemon',name="pokemon",caption='Yeei',user=self.wangari, date='09-07-2021')

    # def test_save_image(self):
    #     # self.pokemon.save_image()
    #     posts = Post.objects.all()
    #     self.assertEquals(len(posts),1)

    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()

    # def test_delete_image(self):
    #     self.pokemon.save_image()
    #     self.pokemon.delete_image()
    #     posts = Post.objects.all()
    #     self.assertTrue(len(posts)==0)

    # def test_update_caption(self):
    #     self.pokemon.save_image()
    #     result = Post.update_caption(self.pokemon.id, 'have fun playing')
    #     self.assertTrue(result.caption, 'have fun playing')

class ProfileTestCase(TestCase):
    '''
    class that tests functions in class Profile
    '''
    def setUp(self):
        self


    


    
        

    

