# Generated by Django 3.1.7 on 2021-05-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='is_webhook_set',
            field=models.BooleanField(default=False, verbose_name='is_webhook_set'),
        ),
        migrations.AddField(
            model_name='bot',
            name='webhook_result_description',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='webhook_error_description'),
        ),
    ]