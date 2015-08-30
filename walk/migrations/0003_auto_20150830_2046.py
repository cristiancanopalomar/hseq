# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rename


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0002_auto_20150829_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('support', models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/supports/'))),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Support',
                'verbose_name_plural': 'Supports',
            },
        ),
        migrations.AlterModelOptions(
            name='commitments',
            options={'verbose_name': 'Commitment', 'verbose_name_plural': 'Commitments'},
        ),
        migrations.AddField(
            model_name='commitments',
            name='closing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='walks',
            name='image_1',
            field=models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks/')),
        ),
        migrations.AlterField(
            model_name='walks',
            name='image_2',
            field=models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks/'), blank=True),
        ),
        migrations.AlterField(
            model_name='walks',
            name='image_3',
            field=models.ImageField(upload_to=rename.rename_file(b'upload/hseq/walk/walks/'), blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='commitments',
            unique_together=set([('number_walk', 'description', 'user_name')]),
        ),
        migrations.AddField(
            model_name='supports',
            name='commitments',
            field=models.ForeignKey(to='walk.Commitments'),
        ),
    ]
