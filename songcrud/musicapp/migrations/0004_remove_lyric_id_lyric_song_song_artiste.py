# Generated by Django 4.1.2 on 2022-11-01 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0003_rename_message_detail_contactmodel_message"),
    ]

    operations = [
        migrations.RemoveField(model_name="lyric", name="id",),
        migrations.AddField(
            model_name="lyric",
            name="Song",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="musicapp.song",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="song",
            name="Artiste",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="musicapp.artiste",
            ),
            preserve_default=False,
        ),
    ]
