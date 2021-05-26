import random
import string
from unittest import mock

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from django.utils.datetime_safe import datetime

from ..models import NewsItem
from .image_test_util import get_image_file

LETTERS = string.ascii_lowercase


class NewsItemsModelTest(TestCase):
    def test_saving_news_item(self):

        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
            image=get_image_file(),
        )
        news_item_2 = NewsItem.objects.create(
            headline="Aliquam erat volutpat",
            summary="Aliquam erat volutpat. Pellentesque eu accumsan eros. Sed sed diam ante",
            content="Aliquam erat volutpat. Pellentesque eu accumsan eros. Sed sed diam ante. Phasellus suscipit a augue molestie imperdiet. Interdum et malesuada fames ac ante ipsum primis in faucibus",
            image=get_image_file(),
        )
        self.assertEqual(news_item_1, NewsItem.objects.all()[0])

    def test_cannot_save_blank_headline(self):

        with self.assertRaises(ValidationError):
            news_item_1 = NewsItem.objects.create(
                headline="",
                summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
                image=get_image_file(),
            )
            news_item_1.full_clean()

    def test_cannot_save_too_long_headline(self):

        # DOUBLE CHECK THIS TEST seems as if django is raising the validation error for anything over 50 chars?

        test_headline = "".join(random.choice(LETTERS) for i in range(201))
        with self.assertRaises(ValidationError):
            news_item_1 = NewsItem.objects.create(
                headline=test_headline,
                summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
                image=get_image_file(),
            )
            news_item_1.full_clean()

    def test_cannot_save_blank_summary(self):

        with self.assertRaises(ValidationError):
            news_item_1 = NewsItem.objects.create(
                headline="Lorem ipsum dolor sit amet",
                summary="",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
                image=get_image_file(),
            )
            news_item_1.full_clean()

    def test_cannot_save_too_long_summary(self):

        test_summary = "".join(random.choice(LETTERS) for i in range(401))

        with self.assertRaises(ValidationError):
            news_item_1 = NewsItem.objects.create(
                headline="Lorem ipsum dolor sit amet",
                summary=test_summary,
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
                image=get_image_file(),
            )
            news_item_1.full_clean()

    def test_cannot_save_blank_content(self):

        with self.assertRaises(ValidationError):
            news_item_1 = NewsItem.objects.create(
                headline="Lorem ipsum dolor sit amet",
                summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                content="",
                image=get_image_file(),
            )
            news_item_1.full_clean()

    def test_created_date(self):
        testtime = datetime.strptime("2021-04-25", "%Y-%m-%d")
        with mock.patch("django.utils.timezone.now") as mock_now:
            mock_now.return_value = testtime
            news_item_1 = NewsItem.objects.create(
                headline="Lorem ipsum dolor",
                summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
            )
            self.assertEqual(str(news_item_1.created), "2021-04-25 00:00:00")

    def test_release_slug_is_created_correctly(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        self.assertEqual(news_item_1.slug, "lorem-ipsum-dolor")

    def test_release_slug_unique(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
        )
        with self.assertRaises(IntegrityError):
            news_item_2 = NewsItem.objects.create(
                headline="Lorem ipsum dolor",
                summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit",
            )
            news_item_2.full_clean()

    def test_can_save_without_image(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
        )
        self.assertEqual(news_item_1, NewsItem.objects.all()[0])

    def test_get_absolute_url(self):

        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
        )

        self.assertEqual(news_item_1.get_absolute_url(), f"/news/{news_item_1.slug}/")

    def test_str_respresentation(self):
        news_item_1 = NewsItem.objects.create(
            headline="Lorem ipsum dolor",
            summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula vitae purus t",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin varius enim eget velit ultrices semper sit amet non ligula. Aliquam hendrerit felis vehicula ultrices tincidunt",
        )
        self.assertEqual(news_item_1.headline, str(news_item_1))
