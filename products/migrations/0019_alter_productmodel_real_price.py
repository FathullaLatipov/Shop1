# Generated by Django 3.2.5 on 2021-07-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_productmodel_real_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]