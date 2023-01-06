from django.test import TestCase,SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        rs = self.client.get('/')
        self.assertEquals(rs.status_code, 200)