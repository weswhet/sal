# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_auto_20150814_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salsetting',
            name='name',
            field=models.CharField(unique=True, max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='osqueryresult',
            unique_together=set([]),
        ),
    ]
