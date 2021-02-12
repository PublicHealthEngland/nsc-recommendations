# Generated by Django 2.2.11 on 2021-02-11 14:07

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("policy", "0001_initial"),
        ("document", "0002_auto_20210210_1640"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="review",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="documents",
                to="review.Review",
                verbose_name="review",
            ),
        ),
        migrations.CreateModel(
            name="DocumentPolicy",
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
                (
                    "source",
                    models.CharField(
                        choices=[("review", "Review"), ("archive", "Archive")],
                        default="review",
                        max_length=7,
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="document.Document",
                    ),
                ),
                (
                    "policy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="policy.Policy"
                    ),
                ),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="document",
            name="policies",
            field=models.ManyToManyField(
                null=True,
                related_name="policy_documents",
                through="document.DocumentPolicy",
                to="policy.Policy",
            ),
        ),
    ]
