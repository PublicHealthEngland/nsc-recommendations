# Generated by Django 2.2.11 on 2021-02-01 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import django_extensions.db.fields
import simple_history.models

import nsc.document.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("review", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalDocument",
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
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("cover_sheet", "Coversheet"),
                            ("submission_form", "Submission form"),
                            ("evidence_review", "Evidence review"),
                            ("external_review", "External review"),
                        ],
                        max_length=256,
                        verbose_name="type of document",
                    ),
                ),
                ("upload", models.TextField(max_length=100, verbose_name="upload")),
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
                (
                    "review",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="review.Review",
                        verbose_name="review",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical document",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Document",
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
                    "document_type",
                    models.CharField(
                        choices=[
                            ("cover_sheet", "Coversheet"),
                            ("submission_form", "Submission form"),
                            ("evidence_review", "Evidence review"),
                            ("external_review", "External review"),
                        ],
                        max_length=256,
                        verbose_name="type of document",
                    ),
                ),
                (
                    "upload",
                    models.FileField(
                        upload_to=nsc.document.models.document_path,
                        verbose_name="upload",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="review.Review",
                        verbose_name="review",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "documents",
                "ordering": ("name", "pk"),
            },
        ),
    ]
