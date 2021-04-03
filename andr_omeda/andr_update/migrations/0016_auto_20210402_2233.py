# Generated by Django 3.1.7 on 2021-04-02 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andr_update', '0015_auto_20210402_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='andruser',
            name='callback_query',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='callback_query_from', to='andr_update.callbackquery'),
        ),
        migrations.AlterField(
            model_name='andruser',
            name='inline_query',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='inline_query_from', to='andr_update.inlinequery'),
        ),
    ]
