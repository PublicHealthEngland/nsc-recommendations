# Generated by Django 2.2.11 on 2021-02-05 13:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="contact", managers=[("manager", django.db.models.manager.Manager()),],
        ),
    ]
