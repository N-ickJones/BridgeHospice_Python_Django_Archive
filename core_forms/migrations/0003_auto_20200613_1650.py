# Generated by Django 2.2 on 2020-06-13 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_forms', '0002_auto_20200601_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerapplication',
            old_name='email_address',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='volunteerapplication',
            old_name='address',
            new_name='street_address',
        ),
    ]
