# Generated by Django 4.1 on 2022-08-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0027_galx'),
    ]

    operations = [
        migrations.AddField(
            model_name='galx',
            name='t111',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='galx',
            name='t222',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='galx',
            name='t333',
            field=models.CharField(default='', max_length=50),
        ),
    ]
