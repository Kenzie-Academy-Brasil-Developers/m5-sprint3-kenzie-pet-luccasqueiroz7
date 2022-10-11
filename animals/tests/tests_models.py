from django.test import TestCase
from animals.models import Animal

from math import log

from groups.models import Group
from traits.models import Trait


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.animal_data = {
            "name": "Lion",
            "age": 2,
            "weight": 10.5,
            "sex": "Macho",
        }
        # Rever group e traits depois
        cls.animal = Animal.objects.create(**cls.animal_data)

    def test_name_max_length(self):
        max_length = self.animal._meta.get_field("name").max_length

        self.assertEqual(max_length, 50)

    def test_sex_max_length(self):
        max_length = self.animal._meta.get_field("sex").max_length

        self.assertEqual(max_length, 15)

    def test_convert_dog_age_to_human_years(self):
        result = self.animal.convert_dog_age_to_human_years()
        expected = round(16 * log(self.animal.age) + 31)

        self.assertEqual(expected, result)


class AnimalRelationshipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.animal_data = {
            "name": "Lux",
            "age": 3,
            "weight": 11.5,
            "sex": "Femea",
        }

        cls.animal_data_2 = {
            "name": "Apolo",
            "age": 1,
            "weight": 5.5,
            "sex": "Macho",
        }

        cls.group_data = {
            "name": "gato",
            "scientific_name": "felis catus",
        }

        cls.trait_data = {
            "name": "peludo",
        }

        cls.trait_data_2 = {
            "name": "médio porte",
        }

        cls.animal = Animal.objects.create(**cls.animal_data)
        cls.animal_2 = Animal.objects.create(**cls.animal_data_2)
        cls.group = Group.objects.create(**cls.group_data)
        cls.trait = Trait.objects.create(**cls.trait_data)
        cls.trait_2 = Trait.objects.create(**cls.trait_data_2)

    def test_animal_contains_group(self):
        self.animal.group = self.group

        self.assertEqual(self.animal.group, self.group)

    def test_group_contais_animals(self):
        self.animal.group = self.group
        self.animal.save()
        self.animal_2.group = self.group
        self.animal_2.save()

        self.assertEquals(2, self.group.animals.count())

    def test_animal_contais_traits(self):
        self.animal.traits.add(self.trait)
        self.animal.traits.add(self.trait_2)
        self.animal.save()
        self.animal_2.traits.add(self.trait_2)
        self.animal_2.save()

        self.assertEquals(2, self.animal.traits.count())
        self.assertEquals(1, self.animal_2.traits.count())

    def test_trait_contais_animals(self):
        self.animal.traits.add(self.trait)
        self.animal.traits.add(self.trait_2)
        self.animal.save()
        self.animal_2.traits.add(self.trait_2)
        self.animal_2.save()

        self.assertEquals(1, self.trait.animals.count())
        self.assertEquals(2, self.trait_2.animals.count())
