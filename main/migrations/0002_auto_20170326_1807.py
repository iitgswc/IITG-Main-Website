# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(default=b'#', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtramurailCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(default=b'#', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Academic',
            new_name='AcademicAffairs',
        ),
        migrations.RenameModel(
            old_name='Center',
            new_name='AcademicCenter',
        ),
    ]
