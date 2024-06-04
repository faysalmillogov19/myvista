# Generated by Django 4.1 on 2024-05-30 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("employe", "0002_client"),
        ("vehicule", "0002_categorie_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicule",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employe.client",
            ),
        ),
    ]
