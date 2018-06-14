# Generated by Django 2.0.4 on 2018-05-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_film_imgdir'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=200)),
                ('CreditCard', models.CharField(max_length=16)),
            ],
        ),
        migrations.RenameField(
            model_name='film',
            old_name='imgdir',
            new_name='Trailer',
        ),
    ]
