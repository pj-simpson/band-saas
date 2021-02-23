from django.test import TestCase
from ..models import Release

class HomePageTest(TestCase):

    def test_home_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')


class DiscogsPageTest(TestCase):

    def test_discogs_uses_correct_template(self):
        response = self.client.get('/discog/')
        self.assertTemplateUsed(response,'discogs/discography.html')

