# Generated by Django 3.2.10 on 2022-05-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_interface_actions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interface_actions',
            name='contract_description',
        ),
        migrations.RemoveField(
            model_name='interface_actions',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='interface_actions',
            name='production_start_at',
        ),
        migrations.AddField(
            model_name='interface_actions',
            name='doc_link',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Doc Link'),
        ),
    ]