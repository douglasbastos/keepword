# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gostei', models.BooleanField()),
                ('evaluation', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=140)),
                ('level', models.IntegerField()),
                ('score', models.DecimalField(decimal_places=2, max_digits=12)),
                ('answer', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name': 'Frase',
                'verbose_name_plural': 'Frases',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='frase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Word'),
        ),
    ]
