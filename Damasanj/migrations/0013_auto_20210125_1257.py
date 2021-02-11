# Generated by Django 3.1.5 on 2021-01-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0012_auto_20210125_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='F',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='TYPE',
            field=models.CharField(choices=[('دینامیک', 'dynamic'), ('استاتیک', 'static')], default='static', max_length=15, verbose_name='نوع'),
        ),
    ]