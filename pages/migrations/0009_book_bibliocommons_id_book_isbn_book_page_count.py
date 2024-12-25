# Generated by Django 5.1.2 on 2024-12-24 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0008_userfavoritelibrary"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="bibliocommons_id",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="isbn",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="page_count",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
