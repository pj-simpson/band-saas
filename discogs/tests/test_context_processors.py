from django.test import TestCase
from unittest.mock import patch



class ContextProcessorTests(TestCase):

    @patch('discogs.context_processors.site_artist_name')
    def test_context_processor_returns_correct_value(self,mock_site_artist_name):
        mock_site_artist_name.return_value = {'artist':'Testing'}
        response = self.client.get('/')
        self.assertEqual(response.context['artist'], 'Testing')

