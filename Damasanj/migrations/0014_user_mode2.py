# Generated by Django 3.1.5 on 2021-01-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0013_auto_20210125_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mode2',
            field=models.CharField(default='0', max_length=10),
        ),
    ]