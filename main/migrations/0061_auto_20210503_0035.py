# Generated by Django 3.2 on 2021-05-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0060_auto_20210429_1506"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_grandfathered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_premium",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="stripe_customer_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
