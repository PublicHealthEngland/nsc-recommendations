# Generated by Django 2.2.11 on 2021-02-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notify", "0001_initial"),
        ("review", "0008_auto_20210204_1105"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviewstakeholdernotification",
            name="review",
        ),
        migrations.RemoveField(
            model_name="reviewstakeholdernotification",
            name="stakeholder",
        ),
        migrations.AddField(
            model_name="review",
            name="open_consultation_notifications",
            field=models.ManyToManyField(related_name="reviews", to="notify.Email"),
        ),
        migrations.DeleteModel(
            name="ReviewPheCommsNotification",
        ),
        migrations.DeleteModel(
            name="ReviewStakeholderNotification",
        ),
    ]
