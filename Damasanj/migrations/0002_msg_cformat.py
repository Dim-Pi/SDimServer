# Generated by Django 3.1.5 on 2021-01-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='CFormat',
            field=models.CharField(choices=[('in', 'ساخت سرور'), ('db', 'از طرف دیتابیس')], default='in', max_length=2, verbose_name='ساخت'),
        ),
    ]
