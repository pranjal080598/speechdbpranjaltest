# Generated by Django 2.2.19 on 2021-03-26 16:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("validation", "0003_merge_20210326_1021"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="created_by",
            field=models.CharField(
                default="", help_text="The person who filed this issue", max_length=64
            ),
        ),
        migrations.AddField(
            model_name="issue",
            name="created_on",
            field=models.DateField(
                help_text="When was this issue filed?",
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="comment",
            field=models.CharField(
                help_text="The comment left by the validator", max_length=1024
            ),
        ),
    ]
