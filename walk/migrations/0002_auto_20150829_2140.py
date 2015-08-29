# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='walks',
            unique_together=set([('number_walk', 'creation_walks', 'registered')]),
        ),
    ]
