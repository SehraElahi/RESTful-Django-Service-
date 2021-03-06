# Generated by Django 3.0.4 on 2020-03-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20200309_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='Module_name',
            new_name='module_name',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=3, verbose_name='Rating (stars)'),
        ),
    ]
