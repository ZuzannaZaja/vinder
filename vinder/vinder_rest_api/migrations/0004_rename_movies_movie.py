# Generated by Django 3.2.8 on 2021-11-20 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinder_rest_api', '0003_rename_maindb_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
