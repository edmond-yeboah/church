# Generated by Django 3.1.7 on 2021-08-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]