# Generated by Django 4.1.7 on 2023-02-28 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
