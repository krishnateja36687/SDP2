# Generated by Django 3.1.7 on 2021-05-18 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0002_auto_20210518_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='firstname',
            new_name='fullname',
        ),
    ]