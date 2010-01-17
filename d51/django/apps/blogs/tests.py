from django.test import TestCase
from django.test.client import Client
from d51.django.apps.blogs.models import Post
import datetime

class BlogHelper(object):
    def create_post(self, **kwargs):
        defaults = {
            'internal_title':'post 1',
            'display_title':'post 1 display',
            'summary':'this is the summary',
            'content':'this is the content',
            'slug':'post-1',
            'published':datetime.datetime.now()
        }
        defaults.update(kwargs)
        return Post.objects.create(**defaults)

class TestBlogViews(BlogHelper, TestCase):
    def test_gets_200_on_existing_page(self):
        post = self.create_post()
        c = Client()
        results = c.get(post.get_absolute_url())

        self.assertEqual(results.status_code, 200)
        self.assertTrue(isinstance(results.context['post'], Post))

    def test_gets_404_on_future_page(self):
        future = datetime.datetime.now() + datetime.timedelta(days=5)
        post = self.create_post(published=future)
        c = Client()
        results = c.get(post.get_absolute_url())
        self.assertEqual(results.status_code, 404)
