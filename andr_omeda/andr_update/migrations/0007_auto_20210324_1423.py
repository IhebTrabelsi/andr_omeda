# Generated by Django 3.1.7 on 2021-03-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0006_auto_20210323_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='id',
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_id',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False, verbose_name='chat_id'),
        ),
    ]
