# Generated by Django 4.1.2 on 2022-10-18 06:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0013_lyric_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
