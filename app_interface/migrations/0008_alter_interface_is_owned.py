# Generated by Django 3.2.10 on 2021-12-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_interface', '0007_alter_interface_interface_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='is_owned',
            field=models.BooleanField(default=True),
        ),
    ]
