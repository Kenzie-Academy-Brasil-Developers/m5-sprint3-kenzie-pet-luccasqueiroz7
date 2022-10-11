from django.db import models

from math import log


class SexAnimal(models.TextChoices):
    MACHO = "Macho"
    FEMEA = "Femea"
    OTHER = "Não informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15,
        choices=SexAnimal.choices,
        default=SexAnimal.OTHER,
    )

    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="animals",
        null=True,
        blank=True,
    )

    traits = models.ManyToManyField(
        "traits.Trait",
        related_name="animals",
        null=True,
        blank=True,
    )

    def convert_dog_age_to_human_years(self):
        human_age = round(16 * log(self.age) + 31)
        return human_age
