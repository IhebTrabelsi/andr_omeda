# Generated by Django 3.1.7 on 2021-04-03 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0024_auto_20210403_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='andruser',
            name='forwarder',
        ),
        migrations.AddField(
            model_name='andruser',
            name='forwarder_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forward_from', to='andr_update.message'),
        ),
    ]