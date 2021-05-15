# Generated by Django 3.1.7 on 2021-05-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0004_update_uuid'),
        ('andr_bot', '0005_bot_chats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='chats',
            field=models.ManyToManyField(blank=True, related_name='bots', to='andr_update.Chat'),
        ),
    ]
