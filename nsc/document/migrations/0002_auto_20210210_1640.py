# Generated by Django 2.2.11 on 2021-02-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("document", "0001_initial"),
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
                    ("other", "Other"),
                ],
                max_length=256,
                verbose_name="type of document",
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
                    ("other", "Other"),
                ],
                max_length=256,
                verbose_name="type of document",
            ),
        ),
    ]
