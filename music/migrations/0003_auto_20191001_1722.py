# Generated by Django 2.2.5 on 2019-10-02 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=1000, upload_to=''),
        ),
    ]
