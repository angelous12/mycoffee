# Generated by Django 4.0.3 on 2022-03-20 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_product_old_new_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 0, 6, 6, 145289)),
        ),
    ]