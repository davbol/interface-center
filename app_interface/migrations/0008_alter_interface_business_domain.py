# Generated by Django 3.2.10 on 2022-01-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_interface', '0007_alter_interface_business_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='business_domain',
            field=models.CharField(choices=[('A.1 ACME Core', '-A.1 ACME Core'), ('A.2 ACME Partner', '-A.2 ACME Partner'), ('A.2.1 ACME Partner Address', '--A.2.1 ACME ACME Partner Address'), ('A.2.3 ACME Partner Contact', '--A.2.3 ACME Partner Contact'), ('B.1 ACME Contract', '-B.1 ACME Contract'), ('B.2 ACME Offer', '-B.2 ACME Offer'), ('B.2.1 ACME Offer Company', '--B.2.1 ACME Offer Company'), ('C.1 ACME Finance', '-C.1 ACME Finance'), ('C.2 ACME Legal & Compliance', '-C.2 ACME Legal & Compliance'), ('C.2.1 ACME Legal', '--C.2.1 ACME Legal'), ('C.2.2 ACME Compliance', '--C.2 ACME Compliance'), ('D.1 ACME Purchasing', '-D.1 ACME Purchasing')], default=None, max_length=50),
        ),
    ]
