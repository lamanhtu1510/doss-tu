# Generated by Django 3.2.5 on 2021-07-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_voucher_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='min_amount',
        ),
    ]
