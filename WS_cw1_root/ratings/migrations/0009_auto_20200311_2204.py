# Generated by Django 3.0.4 on 2020-03-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0008_auto_20200309_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='mod_code',
            field=models.CharField(default='', max_length=3, unique=True, verbose_name='Module Code'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Module Name'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='prof_id',
            field=models.CharField(default='', max_length=3, unique=True, verbose_name='ID'),
        ),
    ]