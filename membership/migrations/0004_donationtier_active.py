# Generated by Django 4.2.9 on 2024-03-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("membership", "0003_remove_donationtier_lookup_key_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="donationtier",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]