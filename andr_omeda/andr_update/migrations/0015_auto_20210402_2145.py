# Generated by Django 3.1.7 on 2021-04-02 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0014_auto_20210402_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatinvitelink',
            name='chat_member_update',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='invite_link', to='andr_update.chatmemberupdated'),
        ),
    ]