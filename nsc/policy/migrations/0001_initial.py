# Generated by Django 2.2.11 on 2021-02-01 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import django_extensions.db.fields
import simple_history.models

import nsc.utils.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("review", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Policy",
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
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is_active"),
                ),
                (
                    "recommendation",
                    models.BooleanField(default=False, verbose_name="recommendation"),
                ),
                (
                    "last_review",
                    models.DateField(blank=True, null=True, verbose_name="last review"),
                ),
                (
                    "next_review",
                    models.DateField(blank=True, null=True, verbose_name="next review"),
                ),
                (
                    "ages",
                    nsc.utils.forms.ChoiceArrayField(
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
                ("condition", models.TextField(verbose_name="condition name")),
                ("condition_html", models.TextField(verbose_name="HTML condition")),
                ("summary", models.TextField(verbose_name="summary")),
                ("summary_html", models.TextField(verbose_name="HTML summary")),
                ("background", models.TextField(verbose_name="summary")),
                ("background_html", models.TextField(verbose_name="HTML summary")),
                (
                    "keywords",
                    models.TextField(
                        blank=True, default="", verbose_name="Search keywords"
                    ),
                ),
                (
                    "reviews",
                    models.ManyToManyField(
                        related_name="policies",
                        to="review.Review",
                        verbose_name="reviews",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "policies",
                "ordering": ("name", "pk"),
            },
        ),
        migrations.CreateModel(
            name="HistoricalPolicy",
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
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is_active"),
                ),
                (
                    "recommendation",
                    models.BooleanField(default=False, verbose_name="recommendation"),
                ),
                (
                    "last_review",
                    models.DateField(blank=True, null=True, verbose_name="last review"),
                ),
                (
                    "next_review",
                    models.DateField(blank=True, null=True, verbose_name="next review"),
                ),
                (
                    "ages",
                    nsc.utils.forms.ChoiceArrayField(
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
                ("condition", models.TextField(verbose_name="condition name")),
                ("condition_html", models.TextField(verbose_name="HTML condition")),
                ("summary", models.TextField(verbose_name="summary")),
                ("summary_html", models.TextField(verbose_name="HTML summary")),
                ("background", models.TextField(verbose_name="summary")),
                ("background_html", models.TextField(verbose_name="HTML summary")),
                (
                    "keywords",
                    models.TextField(
                        blank=True, default="", verbose_name="Search keywords"
                    ),
                ),
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
                "verbose_name": "historical policy",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
