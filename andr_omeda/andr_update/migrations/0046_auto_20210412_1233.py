# Generated by Django 3.1.7 on 2021-04-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0045_auto_20210410_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inlinequery',
            name='offset',
            field=models.TextField(blank=True, verbose_name='offset'),
        ),
        migrations.AlterField(
            model_name='inlinequery',
            name='query',
            field=models.TextField(blank=True, verbose_name='query'),
        ),
    ]