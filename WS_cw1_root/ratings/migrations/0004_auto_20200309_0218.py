# Generated by Django 3.0.4 on 2020-03-09 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20200309_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='name',
            new_name='Module_name',
        ),
    ]
