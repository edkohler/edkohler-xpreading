# Generated by Django 5.1.2 on 2025-01-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0016_alter_author_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="page_count",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]