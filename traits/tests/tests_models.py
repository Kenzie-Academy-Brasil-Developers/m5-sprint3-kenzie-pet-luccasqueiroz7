from django.test import TestCase
from traits.models import Trait


class TraitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.trait_data = {
            "name": "peludo",
        }

        cls.trait = Trait.objects.create(**cls.trait_data)

    def test_name_max_length(self):
        max_length = self.trait._meta.get_field("name").max_length

        self.assertEqual(max_length, 20)

    def test_name_is_unique(self):
        unique = self.trait._meta.get_field("name").unique

        self.assertTrue(unique)
