from django.test import TestCase

from news.models import NewsItem


class NewsFeedTest(TestCase):

    def test_news_feed_uses_correct_template(self):
        response = self.client.get('/news/')
        self.assertTemplateUsed(response,'news/news_feed.html')

    def test_news_feed_has_correct_nav_menu_context(self):
        response = self.client.get('/news/')
        self.assertEqual(response.context['nav'], 'news')

    def test_news_feed_fetches_news_item_objects(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        response = self.client.get('/news/')
        self.assertEqual(response.context['news_items'][0], news_item_1)

    def test_news_item_page_uses_correct_template(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        response = self.client.get(f'/news/{news_item_1.slug}/')
        self.assertTemplateUsed(response, 'news/news_item.html')

    def test_news_item_page_uses_correct_nav_menu_context(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        response = self.client.get(f'/news/{news_item_1.slug}/')
        self.assertEqual(response.context['nav'], 'news')

    def test_news_item_page_fetches_correct_news_item(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_2 = NewsItem.objects.create(
            headline="Cras hendrerit",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        response = self.client.get(f'/news/{news_item_1.slug}/')
        self.assertEqual(response.context['news_item'], news_item_1)
        self.assertNotEqual(response.context['news_item'], news_item_2)

    def test_news_feed_pagination_only_returns_5_objects(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_2 = NewsItem.objects.create(
            headline="Cras hendrerit",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        news_item_3 = NewsItem.objects.create(
            headline="Testing 3",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_4 = NewsItem.objects.create(
            headline="Cras Testing 4",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        news_item_5 = NewsItem.objects.create(
            headline="Lorem Test 5 dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_6 = NewsItem.objects.create(
            headline="Cras toasting 6",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        response = self.client.get('/news/')
        page_obj = response.context['news_items']
        self.assertEqual(len(page_obj.object_list), 5)

    def test_news_feed_pagination_page_param_returns_correct_number_objects(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_2 = NewsItem.objects.create(
            headline="Cras hendrerit",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        news_item_3 = NewsItem.objects.create(
            headline="Testing 3",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_4 = NewsItem.objects.create(
            headline="Cras Testing 4",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        news_item_5 = NewsItem.objects.create(
            headline="Lorem Test 5 dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        news_item_6 = NewsItem.objects.create(
            headline="Cras toasting 6",
            summary="Cras hendrerit tristique mi in congue",
            content="Cras hendrerit tristique mi in congue. Integer eu dui lorem. Ut fringilla fringilla arcu, ",
        )
        response = self.client.get('/news/?page=2')
        page_obj = response.context['news_items']
        self.assertEqual(len(page_obj.object_list), 1)
