# Generated by Django 4.2.7 on 2023-11-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_capitulo_video_capitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutoriales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='tutoriales')),
                ('description', models.TextField()),
            ],
        ),
    ]
