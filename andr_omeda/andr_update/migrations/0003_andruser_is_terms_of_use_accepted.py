# Generated by Django 3.1.7 on 2021-05-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0002_auto_20210507_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='andruser',
            name='is_terms_of_use_accepted',
            field=models.BooleanField(default=False, verbose_name='supports_inline_queries'),
        ),
    ]
