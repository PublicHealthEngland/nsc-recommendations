# Generated by Django 2.2.9 on 2020-01-29 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import django_extensions.db.fields
import simple_history.models

import nsc.condition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Condition",
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
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="name")),
                (
                    "slug",
                    models.SlugField(max_length=256, unique=True, verbose_name="slug"),
                ),
                (
                    "ages",
                    nsc.condition.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("antenatal", "Antenatal"),
                                ("newborn", "Newborn"),
                                ("child", "Child"),
                                ("adult", "Adult"),
                                ("all", "All ages"),
                            ],
                            max_length=50,
                            verbose_name="age groups",
                        ),
                        size=None,
                    ),
                ),
                ("description", models.TextField(verbose_name="description")),
                ("markup", models.TextField(verbose_name="markup")),
            ],
            options={"ordering": ("name", "pk")},
        ),
        migrations.CreateModel(
            name="HistoricalCondition",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="name")),
                ("slug", models.SlugField(max_length=256, verbose_name="slug")),
                (
                    "ages",
                    nsc.condition.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("antenatal", "Antenatal"),
                                ("newborn", "Newborn"),
                                ("child", "Child"),
                                ("adult", "Adult"),
                                ("all", "All ages"),
                            ],
                            max_length=50,
                            verbose_name="age groups",
                        ),
                        size=None,
                    ),
                ),
                ("description", models.TextField(verbose_name="description")),
                ("markup", models.TextField(verbose_name="markup")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical condition",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]