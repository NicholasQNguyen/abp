# Generated by Django 4.2.9 on 2024-03-23 15:59

from django.db import migrations, models

import pbaabp.models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0002_campaign_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="wordpress_id",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="content",
            field=pbaabp.models.MarkdownField(rendered_field="content_rendered"),
        ),
    ]