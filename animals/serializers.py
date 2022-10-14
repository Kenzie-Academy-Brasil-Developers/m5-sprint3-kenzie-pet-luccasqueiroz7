from rest_framework import serializers
from animals.exceptions import NonUpdatableKeyError

from animals.models import Animal, SexAnimal
from traits.models import Trait
from groups.models import Group
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexAnimal.choices,
        default=SexAnimal.OTHER,
    )

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    age_in_human_years = serializers.SerializerMethodField()

    def get_age_in_human_years(self, obj: Animal):
        return obj.convert_dog_age_to_human_years()

    def create(self, validated_data):

        traits_list = validated_data.pop("traits")
        group = validated_data.pop("group")

        animal = Animal.objects.create(**validated_data)

        group_obj, _ = Group.objects.get_or_create(**group)

        animal.group = group_obj

        for trait_dict in traits_list:
            trait_obj, _ = Trait.objects.get_or_create(**trait_dict)
            animal.traits.add(trait_obj)

        animal.save()

        return animal

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            if key == "traits" or key == "group" or key == "sex":
                msg = f"{key}: You can not update {key} property."
                raise NonUpdatableKeyError(msg)
            setattr(instance, key, value)

        instance.save()

        return instance
