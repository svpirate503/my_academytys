# Generated by Django 4.2.6 on 2023-10-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_leccion_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='video_capitulo',
            field=models.FileField(default='', upload_to='presentacion_del_capitulo'),
            preserve_default=False,
        ),
    ]
