# Generated by Django 3.2.6 on 2021-08-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_categoryhomemodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='wishlist',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
