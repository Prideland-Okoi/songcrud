# Generated by Django 4.1.2 on 2022-10-17 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('released_date', models.DateField()),
                ('likes', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=3000)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]