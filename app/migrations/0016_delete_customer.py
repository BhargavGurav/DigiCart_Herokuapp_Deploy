# Generated by Django 4.0.3 on 2022-08-20 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_customer_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
