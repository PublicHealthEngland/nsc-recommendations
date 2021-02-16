# Generated by Django 2.2.11 on 2021-02-12 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("document", "0004_merge_20210211_1420"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="document_type",
            field=models.CharField(
                choices=[
                    ("cover_sheet", "Coversheet"),
                    ("submission_form", "Submission form"),
                    ("evidence_review", "Evidence review"),
                    ("evidence_map", "Evidence map"),
                    ("cost", "Cost-effective model"),
                    ("systematic", "Systematic review"),
                    ("external_review", "External review"),
                    ("archive", "Archive"),
                    ("other", "Other"),
                ],
                max_length=256,
                verbose_name="type of document",
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="review",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="documents",
                to="review.Review",
                verbose_name="review",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldocument",
            name="document_type",
            field=models.CharField(
                choices=[
                    ("cover_sheet", "Coversheet"),
                    ("submission_form", "Submission form"),
                    ("evidence_review", "Evidence review"),
                    ("evidence_map", "Evidence map"),
                    ("cost", "Cost-effective model"),
                    ("systematic", "Systematic review"),
                    ("external_review", "External review"),
                    ("archive", "Archive"),
                    ("other", "Other"),
                ],
                max_length=256,
                verbose_name="type of document",
            ),
        ),
    ]