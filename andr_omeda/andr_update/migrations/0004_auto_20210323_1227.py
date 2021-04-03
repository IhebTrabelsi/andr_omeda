# Generated by Django 3.1.7 on 2021-03-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0003_auto_20210323_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='channel_chat_created',
            field=models.BooleanField(blank=True, null=True, verbose_name='channel_chat_created'),
        ),
        migrations.AlterField(
            model_name='message',
            name='delete_chat_photo',
            field=models.BooleanField(blank=True, null=True, verbose_name='delete_chat_photo'),
        ),
        migrations.AlterField(
            model_name='message',
            name='edit_date',
            field=models.IntegerField(blank=True, null=True, verbose_name='edit_date'),
        ),
        migrations.AlterField(
            model_name='message',
            name='forward_date',
            field=models.IntegerField(blank=True, null=True, verbose_name='forward_date'),
        ),
        migrations.AlterField(
            model_name='message',
            name='forward_from_message_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='forward_from_message_id'),
        ),
        migrations.AlterField(
            model_name='message',
            name='group_chat_created',
            field=models.BooleanField(blank=True, null=True, verbose_name='group_chat_created'),
        ),
        migrations.AlterField(
            model_name='message',
            name='migrate_from_chat_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='migrate_from_chat_id'),
        ),
        migrations.AlterField(
            model_name='message',
            name='migrate_to_chat_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='migrate_to_chat_id'),
        ),
        migrations.AlterField(
            model_name='message',
            name='supergroup_chat_created',
            field=models.BooleanField(blank=True, null=True, verbose_name='supergroup_chat_created'),
        ),
    ]
