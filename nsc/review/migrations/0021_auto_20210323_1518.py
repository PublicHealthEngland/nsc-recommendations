# Generated by Django 2.2.11 on 2021-03-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0020_auto_20210219_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreview',
            name='is_legacy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='is_legacy',
            field=models.BooleanField(default=False),
        ),
    ]
