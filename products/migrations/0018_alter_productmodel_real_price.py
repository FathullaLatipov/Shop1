# Generated by Django 3.2.5 on 2021-07-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_productmodel_real_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='real_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='real price'),
        ),
    ]
