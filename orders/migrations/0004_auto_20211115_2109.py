# Generated by Django 3.2.6 on 2021-11-15 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210726_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='zip',
        ),
    ]