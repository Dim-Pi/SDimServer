# Generated by Django 3.1.5 on 2021-01-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0011_auto_20210125_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nmod',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='nmods',
            field=models.TextField(default=''),
        ),
    ]