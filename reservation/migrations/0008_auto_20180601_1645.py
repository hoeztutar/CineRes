# Generated by Django 2.0.4 on 2018-06-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_auto_20180601_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audi',
            name='audiNoSeats',
            field=models.IntegerField(),
        ),
    ]
