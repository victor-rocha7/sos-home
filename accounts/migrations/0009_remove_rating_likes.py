# Generated by Django 4.1.3 on 2022-12-03 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_rating_author_alter_rating_profile"),
    ]

    operations = [
        migrations.RemoveField(model_name="rating", name="likes",),
    ]
