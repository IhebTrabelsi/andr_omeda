# Generated by Django 3.1.7 on 2021-05-10 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andr_bot', '0003_bot_tableau'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='tableau',
        ),
    ]
