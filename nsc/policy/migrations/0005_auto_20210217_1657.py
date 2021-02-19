# Generated by Django 2.2.11 on 2021-02-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("policy", "0004_auto_20210215_1410"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpolicy",
            name="background",
            field=models.TextField(verbose_name="background"),
        ),
        migrations.AlterField(
            model_name="historicalpolicy",
            name="background_html",
            field=models.TextField(verbose_name="HTML background"),
        ),
        migrations.AlterField(
            model_name="historicalpolicy",
            name="recommendation",
            field=models.NullBooleanField(default=None, verbose_name="recommendation"),
        ),
        migrations.AlterField(
            model_name="policy",
            name="background",
            field=models.TextField(verbose_name="background"),
        ),
        migrations.AlterField(
            model_name="policy",
            name="background_html",
            field=models.TextField(verbose_name="HTML background"),
        ),
        migrations.AlterField(
            model_name="policy",
            name="recommendation",
            field=models.NullBooleanField(default=None, verbose_name="recommendation"),
        ),
    ]
