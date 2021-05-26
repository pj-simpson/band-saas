from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from news.tests.image_test_util import get_image_file

from ..models import Release


class ReleaseModelTest(TestCase):
    def test_saving_release(self):
        release1 = Release.objects.create(
            title="a new title",
            info="blah blah blah",
            release_date="2020-02-01",
            image=get_image_file(),
            link="https://link.com",
        )
        release2 = Release.objects.create(
            title="a newer title",
            info="blah blah blah",
            release_date="2020-02-02",
            image=get_image_file(),
            link="https://link.com",
        )
        self.assertEqual(release1, Release.objects.all()[0])

    def test_cannot_save_blank_release_title(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(
                title="",
                info="blah blah blah",
                release_date="2020-02-01",
                image=get_image_file(),
                link="https://link.com",
            )
            release1.full_clean()

    def test_cannot_save_blank_release_date(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(
                title="a new title",
                info="blah blah blah",
                release_date="",
                image=get_image_file(),
                link="https://link.com",
            )
            release1.full_clean()

    def test_cannot_save_long_release_title(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(
                title="f73qOnwrKNa2ParujmRMwYL34ULi29xXLXFFslp0hbRNzClOQaYrBX0Mrwwp3CnfNVegcAbOdD1mzqGl4iVThHl1Mcrpa9V4PYCNcgiHUq7r8h6fQqf70hgA1yD8LxpwCyDcae3EGmlC2q27uoklhN7ag9ysWef6MCkMJw3YU1t034FJnoN2OKByl26fjqTc15X1uOaff0",
                info="blah blah blah",
                release_date="2020-02-01",
                image=get_image_file(),
                link="https://link.com",
            )
            release1.full_clean()

    def test_cannot_save_improperly_formatted_release_date(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(
                title="a new title",
                info="blah blah blah",
                release_date="400",
                image=get_image_file(),
                link="https://link.com",
            )
            release1.full_clean()

    def test_can_save_blank_info(self):
        release1 = Release.objects.create(
            title="a new title",
            info="",
            release_date="2020-02-01",
            image=get_image_file(),
            link="https://link.com",
        )
        self.assertEqual(release1, Release.objects.all()[0])

    def test_can_save_blank_image(self):
        release1 = Release.objects.create(
            title="a new title",
            info="",
            release_date="2020-02-01",
            link="https://link.com",
        )
        self.assertEqual(release1, Release.objects.all()[0])

    def test_can_save_blank_link(self):
        release1 = Release.objects.create(
            title="a new title",
            info="",
            release_date="2020-02-01",
            image=get_image_file(),
        )
        self.assertEqual(release1, Release.objects.all()[0])

    def test_cannot_save_improperly_formatted_link(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(
                title="a new title", info="", release_date="2020-02-01", link="link_com"
            )
            release1.full_clean()

    def test_release_slug_is_created_correctly(self):
        release1 = Release.objects.create(
            title="a new title",
            info="blah",
            release_date="2020-02-01",
            image=get_image_file(),
            link="https://link.com",
        )
        self.assertEqual(release1.slug, "a-new-title")

    def test_release_slug_unique(self):
        release1 = Release.objects.create(
            title="a new title", info="blah", release_date="2020-02-01"
        )
        with self.assertRaises(IntegrityError):
            release2 = Release.objects.create(
                title="a new title", info="blah blah blah", release_date="2020-03-01"
            )
            release2.full_clean()

    def test_get_absolute_url(self):
        release1 = Release.objects.create(
            title="a new title",
            info="blah",
            release_date="2020-02-01",
            image=get_image_file(),
            link="https://link.com",
        )
        self.assertEqual(release1.get_absolute_url(), f"/discog/{release1.slug}/")

    def test_str_respresentation(self):
        release1 = Release.objects.create(
            title="a new title", info="blah", release_date="2020-02-01"
        )
        self.assertEqual(release1.title, str(release1))
