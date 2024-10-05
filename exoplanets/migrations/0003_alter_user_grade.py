# Generated by Django 5.1.1 on 2024-10-03 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exoplanets", "0002_category_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="grade",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(14),
                    django.core.validators.MinValueValidator(1),
                ]
            ),
        ),
    ]
