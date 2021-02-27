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

    def test_release_page_uses_correct_template(self):
        release1 = Release.objects.create(title="a new title", info="blah blah blah", release_date='2020-02-01')
        response = self.client.get('/discog/a-new-title/')
        self.assertTemplateUsed(response,'discogs/release.html')

    def test_release_page_fetches_correct_release(self):
        release1 = Release.objects.create(title="a new title", info="blah blah blah", release_date='2020-02-01')
        release2 = Release.objects.create(title="a second", info="rah rah rah", release_date='2022-02-01')
        response = self.client.get('/discog/a-new-title/')
        self.assertEqual(response.context['release'], release1)
        self.assertNotEqual(response.context['release'], release2)

