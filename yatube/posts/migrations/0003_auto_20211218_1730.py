# Generated by Django 2.2.19 on 2021-12-18 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211218_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Groups',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='group',
            new_name='groups',
        ),
    ]
