from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

from .models import Post

class BlogTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.user = get_user_model().objects.create_user(
      username='testuser',
      email = 'testuser@example.com',
      password = 'testpassword'
    )
    
    cls.post = Post.objects.create(
      user = cls.user,
      title = 'Test post',
      content = 'Test body'
    )
    
  def test_post_model(self):
    self.assertEqual(self.post.user.username, "testuser")
    self.assertEqual(self.post.title, 'Test post')
    self.assertEqual(self.post.content, 'Test body')
    self.assertEqual(str(self.post), "Test post by testuser")
