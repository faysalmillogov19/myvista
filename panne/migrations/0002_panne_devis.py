# Generated by Django 4.1 on 2024-05-23 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garage", "0001_initial"),
        ("vehicule", "0002_categorie_description"),
        ("panne", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Panne",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pieces", models.TextField()),
                ("description", models.TextField(null=True)),
                ("date", models.DateField(null=True)),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panne.type",
                    ),
                ),
                (
                    "vehicule",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicule.vehicule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Devis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "proforma",
                    models.FileField(
                        max_length=254, null=True, upload_to="panne/proforma/"
                    ),
                ),
                (
                    "facture",
                    models.FileField(
                        max_length=254, null=True, upload_to="panne/facture/"
                    ),
                ),
                ("cout", models.FloatField()),
                ("date", models.DateField(null=True)),
                ("accepter", models.BooleanField(default=False)),
                (
                    "garage",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="garage.garage",
                    ),
                ),
                (
                    "panne",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panne.panne",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="panne.type",
                    ),
                ),
            ],
        ),
    ]