# Generated by Django 4.0.2 on 2022-03-17 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 17, 23, 21, 8, 926472))),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
