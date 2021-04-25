from django.test import TestCase

class NewsFeedTest(TestCase):

    def test_news_feed_uses_correct_template(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response,'news/news_feed.html')

    def test_news_feed_has_correct_nav_menu_context(self):
        response = self.client.get('/news/')
        self.assertEqual(response.context['nav'], 'news')

    # def test_discogs_fetches_release_objects(self):
    #     newsitem1 = NewsItem.objects.create()
    #     response = self.client.get('/news/')
    #     self.assertEqual(response.context['news_items'][0], newsitem1)