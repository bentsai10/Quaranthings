# Generated by Django 2.2 on 2020-08-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quaranthings', '0011_auto_20200820_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
