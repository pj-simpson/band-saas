from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Release


class ReleaseModelTest(TestCase):

    def test_saving_release(self):
        release1 = Release.objects.create(title="a new title",info="blah blah blah",release_date='2020-02-01')
        release2 = Release.objects.create(title="a newer title", info="blah blah blah", release_date='2020-02-02')
        self.assertEqual(release1,Release.objects.all()[0])

    def test_cannot_save_blank_release_title(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(title="", info="blah blah blah", release_date='2020-02-01')
            release1.full_clean()

    def test_cannot_save_blank_release_date(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(title="a new title", info="blah blah blah", release_date='')
            release1.full_clean()

    def test_cannot_save_long_release_title(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(title="f73qOnwrKNa2ParujmRMwYL34ULi29xXLXFFslp0hbRNzClOQaYrBX0Mrwwp3CnfNVegcAbOdD1mzqGl4iVThHl1Mcrpa9V4PYCNcgiHUq7r8h6fQqf70hgA1yD8LxpwCyDcae3EGmlC2q27uoklhN7ag9ysWef6MCkMJw3YU1t034FJnoN2OKByl26fjqTc15X1uOaff0", info="blah blah blah", release_date='2020-02-01')
            release1.full_clean()

    def test_cannot_save_improperly_formatted_release_date(self):
        with self.assertRaises(ValidationError):
            release1 = Release.objects.create(title="a new title", info="blah blah blah", release_date='400')
            release1.full_clean()

    def test_can_save_blank_info(self):
        release1 = Release.objects.create(title="a new title",info="",release_date='2020-02-01')
        self.assertEqual(release1,Release.objects.all()[0])


