# Generated by Django 3.1.7 on 2021-05-11 09:57

import andr_omeda.andr_record.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_record', '0006_auto_20210511_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowqueue',
            name='queue',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=andr_omeda.andr_record.models._def_queue, size=None),
        ),
    ]