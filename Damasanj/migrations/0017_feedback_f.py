# Generated by Django 3.1.5 on 2021-01-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Damasanj', '0016_remove_feedback_f'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='F',
            field=models.CharField(default=None, max_length=100),
        ),
    ]