# Generated by Django 3.2.10 on 2022-01-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_interface', '0014_interface_owner_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='restriction_code',
            field=models.CharField(blank=True, choices=[('NUTZUNG', 'NUTZUNG'), ('TEST', 'TEST')], default=None, max_length=20, null=True),
        ),
    ]
