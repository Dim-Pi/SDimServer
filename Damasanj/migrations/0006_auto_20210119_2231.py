# Generated by Django 3.1.5 on 2021-01-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0005_auto_20210119_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lmod',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='lmods',
            field=models.TextField(default='', verbose_name='ماد قبلی'),
        ),
    ]