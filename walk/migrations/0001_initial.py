# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import rename


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Findings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Finding',
                'verbose_name_plural': 'Findings',
            },
        ),
        migrations.CreateModel(
            name='Walks',
            fields=[
                ('number_walk', models.CharField(help_text=b'number of walk', max_length=15, unique=True, serialize=False, primary_key=True)),
                ('creation_walks', models.DateTimeField(help_text=b'item creation date', verbose_name='creation date', auto_now_add=True)),
                ('company', models.CharField(max_length=4, choices=[(b'C-OI', b'cam, operaci\xc3\xb3n integral'), (b'M-OI', b'micol, operaci\xc3\xb3n integral'), (b'W-OI', b'WSP, operaci\xc3\xb3n integral')])),
                ('activity', models.CharField(max_length=50)),
                ('place', models.PositiveIntegerField()),
                ('accomplished', models.CharField(max_length=20, verbose_name='accomplished by')),
                ('responsible', models.CharField(max_length=20, verbose_name='responsible of activity')),
                ('good_practices', models.TextField()),
                ('comments_findings', models.TextField(help_text=b'comments of findings')),
                ('feedback_comments', models.TextField(help_text=b'feedback and comments')),
                ('image_1', models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks'))),
                ('image_2', models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks'), blank=True)),
                ('image_3', models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks'), blank=True)),
                ('accompaniment', models.CharField(max_length=25, blank=True)),
                ('findings', models.ManyToManyField(help_text=b'characterization of the findings', to='walk.Findings')),
                ('registered', models.ForeignKey(help_text=b'registrado by user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Walk',
                'verbose_name_plural': 'Walks',
            },
        ),
        migrations.AlterUniqueTogether(
            name='findings',
            unique_together=set([('description',)]),
        ),
        migrations.AddField(
            model_name='commitments',
            name='number_walk',
            field=models.ForeignKey(to='walk.Walks'),
        ),
        migrations.AlterUniqueTogether(
            name='walks',
            unique_together=set([('number_walk', 'creation_walks')]),
        ),
    ]
