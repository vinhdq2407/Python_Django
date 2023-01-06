from django.test import TestCase
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    def setUp(seft):
        Post.objects.create(
            title= "myTitle",
            body='just a Test'
        )
    def test_str_representation(self):
        post = Post(title='My entry title')
        self.assertEquals(str(post),post.title)
    def test_post_list_view(self):
        rs = self.client.get('/blog/')
        self.assertEquals(rs.status_code,200)
        self.assertContains(rs,'myTitle')
        self.assertTemplateUsed(rs,'blog/blog.html')
    def test_post_detail_view(self):
        rs = self.client.get('/blog/1/')
        self.assertEquals(rs.status_code,200)
        self.assertContains(rs,'myTitle')
        self.assertTemplateUsed(rs,'blog/post.html')