# Generated by Django 4.2.7 on 2023-11-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_tutoriales'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoriales',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='thumbnail'),
            preserve_default=False,
        ),
    ]
