# Generated by Django 3.1.7 on 2021-08-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210727_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=50, null=True)),
                ('verse', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]