# Generated by Django 3.0.4 on 2020-03-09 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='mod_code',
            new_name='module_code',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='prof_id',
            new_name='professor_id',
        ),
    ]
