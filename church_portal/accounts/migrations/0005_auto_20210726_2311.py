# Generated by Django 3.1.7 on 2021-07-26 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210725_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusers',
            name='child',
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='father',
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='gfather',
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='gmother',
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='mother',
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='spouse',
        ),
    ]