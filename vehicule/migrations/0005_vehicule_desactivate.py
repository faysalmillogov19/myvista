# Generated by Django 5.0.6 on 2024-06-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicule", "0004_remove_vehicule_client_vehicule_proprio"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicule",
            name="desactivate",
            field=models.BooleanField(default=False),
        ),
    ]