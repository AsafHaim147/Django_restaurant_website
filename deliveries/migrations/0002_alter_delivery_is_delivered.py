# Generated by Django 4.2 on 2023-04-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='is_delivered',
            field=models.BooleanField(null=True),
        ),
    ]
