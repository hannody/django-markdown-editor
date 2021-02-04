from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):
        
        # Create a post object with some data
        post = Post(title='My Title', description = 'Blurb', wiki= 'Post Body')

        # Check that the values match expectations
        self.assertEqual(post.title, 'My Title')
        self.assertEqual(post.description, 'Blurb')
        self.assertEqual(post.wiki, 'Post Body')
