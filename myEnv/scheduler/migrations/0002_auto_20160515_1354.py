# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
