# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-24 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0002_auto_20160817_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActStat',
            fields=[
                ('actstatid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса (ключ)')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы актуальности ФИАС',
                'verbose_name': 'Статус актуальности ФИАС',
            },
        ),
        migrations.CreateModel(
            name='CenterSt',
            fields=[
                ('centerstid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы центров',
                'verbose_name': 'Статус центра',
            },
        ),
        migrations.CreateModel(
            name='CurentSt',
            fields=[
                ('curentstid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса (ключ)')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы актуальности КЛАДР 4.0',
                'verbose_name': 'Статус актуальности КЛАДР 4.0',
            },
        ),
        migrations.CreateModel(
            name='EstStat',
            fields=[
                ('eststatid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Признак владения')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('shortname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Краткое наименование')),
            ],
            options={
                'verbose_name_plural': 'Признаки владения',
                'verbose_name': 'Признак владения',
            },
        ),
        migrations.CreateModel(
            name='HSTStat',
            fields=[
                ('housestid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса')),
                ('name', models.CharField(max_length=60, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы состояния домов',
                'verbose_name': 'Статус состояния домов',
            },
        ),
        migrations.CreateModel(
            name='IntvStat',
            fields=[
                ('intvstatid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса (обычный, четный, нечетный)')),
                ('name', models.CharField(max_length=60, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы интервалов домов',
                'verbose_name': 'Статус интервала домов',
            },
        ),
        migrations.CreateModel(
            name='NDocType',
            fields=[
                ('ndtypeid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор записи (ключ)')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование типа нормативного документа')),
            ],
            options={
                'verbose_name_plural': 'Типы нормативных документов',
                'verbose_name': 'Тип нормативного документа',
            },
        ),
        migrations.CreateModel(
            name='OperStat',
            fields=[
                ('operstatid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор статуса (ключ)')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Статусы действия',
                'verbose_name': 'Статус действия',
            },
        ),
        migrations.CreateModel(
            name='StrStat',
            fields=[
                ('strstatid', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Признак строения')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('shortname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Краткое наименование')),
            ],
            options={
                'verbose_name_plural': 'Признаки строения',
                'verbose_name': 'Признак строения',
            },
        ),
    ]