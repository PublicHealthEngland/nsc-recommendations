# Generated by Django 2.2.9 on 2020-02-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("policy", "0002_auto_20200206_1043")]

    operations = [
        migrations.AddField(
            model_name="historicalpolicy",
            name="keywords",
            field=models.TextField(
                blank=True, default="", verbose_name="Search keywords"
            ),
        ),
        migrations.AddField(
            model_name="policy",
            name="keywords",
            field=models.TextField(
                blank=True, default="", verbose_name="Search keywords"
            ),
        ),
    ]
