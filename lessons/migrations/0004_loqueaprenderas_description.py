# Generated by Django 4.2.6 on 2023-10-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_loqueaprenderas'),
    ]

    operations = [
        migrations.AddField(
            model_name='loqueaprenderas',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
