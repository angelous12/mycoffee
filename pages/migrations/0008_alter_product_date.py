# Generated by Django 4.0.3 on 2022-03-21 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_product_slug_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 3, 55, 34, 131321)),
        ),
    ]
