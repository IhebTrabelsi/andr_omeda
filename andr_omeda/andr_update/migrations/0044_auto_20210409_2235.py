# Generated by Django 3.1.7 on 2021-04-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0043_auto_20210409_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmember',
            name='new_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='new_chat_member', to='andr_update.chatmemberupdated'),
        ),
        migrations.AlterField(
            model_name='chatmember',
            name='old_member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='old_chat_member', to='andr_update.chatmemberupdated'),
        ),
    ]