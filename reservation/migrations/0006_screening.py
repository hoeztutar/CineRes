# Generated by Django 2.0.4 on 2018-06-01 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20180516_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('audi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Audi')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Film')),
            ],
        ),
    ]
