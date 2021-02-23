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

    def test_discogs_fetches_release_objects(self):
        release1 = Release.objects.create(title="a new title",info="blah blah blah",release_date='2020-02-01')
        response = self.client.get('/discog/')
        self.assertEqual(response.context['releases'][0], release1)

