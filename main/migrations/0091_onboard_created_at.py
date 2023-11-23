# Generated by Django 4.2.7 on 2023-11-09 20:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0090_onboard"),
    ]

    operations = [
        migrations.AddField(
            model_name="onboard",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]