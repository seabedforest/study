# Generated by Django 2.2.12 on 2020-07-28 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200728_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='avator',
            new_name='avatar',
        ),
    ]
