# Generated by Django 3.1.5 on 2021-01-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0014_user_mode2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sign2',
            field=models.BooleanField(default=False),
        ),
    ]