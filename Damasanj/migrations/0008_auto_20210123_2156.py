# Generated by Django 3.1.5 on 2021-01-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0007_role_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='options',
            field=models.CharField(default='e', max_length=1, verbose_name='دسترسی'),
        ),
        migrations.AddField(
            model_name='role',
            name='optionsave',
            field=models.TextField(default='e'),
        ),
    ]