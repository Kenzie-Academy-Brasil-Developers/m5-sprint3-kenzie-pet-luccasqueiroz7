from django.test import TestCase
from groups.models import Group


class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.group_data = {
            "name": "gato",
            "scientific_name": "felis catus",
        }

        cls.group = Group.objects.create(**cls.group_data)

    def test_name_max_length(self):
        max_length = self.group._meta.get_field("name").max_length

        self.assertEqual(max_length, 20)

    def test_name_is_unique(self):
        unique = self.group._meta.get_field("name").unique

        self.assertTrue(unique)

    def test_scientific_name_max_length(self):
        max_length = self.group._meta.get_field("scientific_name").max_length

        self.assertEqual(max_length, 50)

    def test_scientific_name_is_unique(self):
        unique = self.group._meta.get_field("scientific_name").unique

        self.assertTrue(unique)
