# Generated by Django 4.2.6 on 2023-10-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_remove_compra_customer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='customer_id_stripe',
        ),
        migrations.AddField(
            model_name='compra',
            name='customer_email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
