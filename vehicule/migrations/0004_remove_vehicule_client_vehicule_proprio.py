# Generated by Django 4.1 on 2024-05-31 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vehicule", "0003_vehicule_client"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicule",
            name="client",
        ),
        migrations.AddField(
            model_name="vehicule",
            name="proprio",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
