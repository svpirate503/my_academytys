# Generated by Django 4.2.7 on 2023-11-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatars'),
            preserve_default=False,
        ),
    ]
