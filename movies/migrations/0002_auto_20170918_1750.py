# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row1_place1', models.BooleanField(default=False)),
                ('row1_place2', models.BooleanField(default=False)),
                ('row1_place3', models.BooleanField(default=False)),
                ('row1_place4', models.BooleanField(default=False)),
                ('row1_place5', models.BooleanField(default=False)),
                ('row1_place6', models.BooleanField(default=False)),
                ('row1_place7', models.BooleanField(default=False)),
                ('row1_place8', models.BooleanField(default=False)),
                ('row2_place1', models.BooleanField(default=False)),
                ('row2_place2', models.BooleanField(default=False)),
                ('row2_place3', models.BooleanField(default=False)),
                ('row2_place4', models.BooleanField(default=False)),
                ('row2_place5', models.BooleanField(default=False)),
                ('row2_place6', models.BooleanField(default=False)),
                ('row2_place7', models.BooleanField(default=False)),
                ('row2_place8', models.BooleanField(default=False)),
                ('row3_place1', models.BooleanField(default=False)),
                ('row3_place2', models.BooleanField(default=False)),
                ('row3_place3', models.BooleanField(default=False)),
                ('row3_place4', models.BooleanField(default=False)),
                ('row3_place5', models.BooleanField(default=False)),
                ('row3_place6', models.BooleanField(default=False)),
                ('row3_place7', models.BooleanField(default=False)),
                ('row3_place8', models.BooleanField(default=False)),
                ('row4_place1', models.BooleanField(default=False)),
                ('row4_place2', models.BooleanField(default=False)),
                ('row4_place3', models.BooleanField(default=False)),
                ('row4_place4', models.BooleanField(default=False)),
                ('row4_place5', models.BooleanField(default=False)),
                ('row4_place6', models.BooleanField(default=False)),
                ('row4_place7', models.BooleanField(default=False)),
                ('row4_place8', models.BooleanField(default=False)),
                ('row5_place1', models.BooleanField(default=False)),
                ('row5_place2', models.BooleanField(default=False)),
                ('row5_place3', models.BooleanField(default=False)),
                ('row5_place4', models.BooleanField(default=False)),
                ('row5_place5', models.BooleanField(default=False)),
                ('row5_place6', models.BooleanField(default=False)),
                ('row5_place7', models.BooleanField(default=False)),
                ('row5_place8', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=0, upload_to='movies/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=0, help_text='A short label, generally used in URLs.', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.PositiveSmallIntegerField(help_text='Film duration, in minutes.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('action', 'Action'), ('adventure', 'Adventure'), ('crime', 'Crime'), ('drama', 'Drama')], max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=models.PositiveSmallIntegerField(help_text='Price of one ticket, in dollars.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(help_text='When film was releaded.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='start_time',
            field=models.DateTimeField(help_text='When film will be show in cinema.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='places',
            name='chain_models',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]
