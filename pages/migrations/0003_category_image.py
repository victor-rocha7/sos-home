# Generated by Django 4.1.3 on 2022-11-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_delete_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.URLField(
                default="https://www.ncenet.com/wp-content/uploads/2020/04/No-image-found.jpg"
            ),
        ),
    ]
