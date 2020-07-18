# Generated by Django 2.2.12 on 2020-07-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11)),
                ('avatar', models.FileField(upload_to='avatar')),
            ],
        ),
    ]
