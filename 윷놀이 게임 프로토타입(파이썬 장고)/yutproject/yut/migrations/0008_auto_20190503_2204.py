# Generated by Django 2.2.1 on 2019-05-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yut', '0007_auto_20190503_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horse',
            old_name='name',
            new_name='player_name',
        ),
        migrations.AddField(
            model_name='horse',
            name='horse_number',
            field=models.IntegerField(default=0),
        ),
    ]
