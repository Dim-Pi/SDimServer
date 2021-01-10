# Generated by Django 3.0.5 on 2021-01-10 13:39

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('topics', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('Sname', models.CharField(max_length=220)),
                ('Bname', models.CharField(max_length=220)),
                ('stuid', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('Sid', models.CharField(max_length=200)),
                ('model', models.CharField(choices=[['dmn', 'dmn'], ['Bdmn', 'Bdmn'], ['stu', 'stu']], max_length=6)),
                ('mode', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField(blank=True)),
                ('text', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Damasanj.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='dadmin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Damasanj.user'),
        ),
        migrations.CreateModel(
            name='dor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strart', models.TimeField()),
                ('finish', models.TimeField()),
                ('topic', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('qtion', django.contrib.postgres.fields.hstore.HStoreField()),
                ('toool', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Damasanj.user')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Damasanj.Lesson')),
            ],
        ),
    ]
