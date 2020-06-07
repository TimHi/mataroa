# Generated by Django 3.0.7 on 2020-06-07 20:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_post_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateField(
                blank=True,
                default=django.utils.timezone.now,
                help_text="Leave blank to keep as draft/unpublished",
                null=True,
            ),
        ),
    ]
