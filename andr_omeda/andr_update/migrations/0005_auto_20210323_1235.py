# Generated by Django 3.1.7 on 2021-03-23 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0004_auto_20210323_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='callbackquery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='andr_update.callbackquery'),
        ),
        migrations.AlterField(
            model_name='message',
            name='forward_from_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='forwarded_messages', to='andr_update.chat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='pinned_message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='andr_update.message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='reply_to_message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='andr_update.message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='sended_messages', to='andr_update.chat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='update',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='andr_update.update'),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_for_this_channel_post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_post', to='andr_update.update'),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_for_this_edited_channel_post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_channel_post', to='andr_update.update'),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_for_this_edited_message',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_message', to='andr_update.update'),
        ),
    ]
