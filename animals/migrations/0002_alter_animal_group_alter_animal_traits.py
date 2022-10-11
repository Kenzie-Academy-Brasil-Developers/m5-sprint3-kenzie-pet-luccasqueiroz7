# Generated by Django 4.1.2 on 2022-10-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0003_alter_group_scientific_name"),
        ("traits", "0001_initial"),
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animals",
                to="groups.group",
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="traits",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="animals", to="traits.trait"
            ),
        ),
    ]
