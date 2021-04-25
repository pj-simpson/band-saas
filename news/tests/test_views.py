from django.test import TestCase

from news.models import NewsItem


class NewsFeedTest(TestCase):

    def test_news_feed_uses_correct_template(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response,'news/news_feed.html')

    def test_news_feed_has_correct_nav_menu_context(self):
        response = self.client.get('/news/')
        self.assertEqual(response.context['nav'], 'news')

    def test_news_item_fetches_news_item_objects(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        response = self.client.get('/news/')
        self.assertEqual(response.context['news_items'][0], news_item_1)