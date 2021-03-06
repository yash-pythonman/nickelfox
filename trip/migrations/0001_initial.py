# Generated by Django 3.1.3 on 2021-09-09 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0002_auto_20210909_2111"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "traveler",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips_of_traveler",
                        to="user.user",
                    ),
                ),
                (
                    "trip_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="trip_on_from_address",
                        to="order.address",
                    ),
                ),
                (
                    "trip_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="trip_on_to_address",
                        to="order.address",
                    ),
                ),
            ],
            options={"db_table": "trip",},
        ),
    ]
