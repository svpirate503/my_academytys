# Generated by Django 4.2.6 on 2023-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_remove_loqueaprenderas_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]