# Generated by Django 4.1.2 on 2022-10-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0009_alter_artist_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lyrics',
            new_name='Lyric',
        ),
    ]