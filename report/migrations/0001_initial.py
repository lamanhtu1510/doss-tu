# Generated by Django 3.2.2 on 2021-08-09 18:21

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0004_auto_20210709_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReport',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('order.orderdetail',),
        ),
        migrations.CreateModel(
            name='SalesReport',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('order.order',),
        ),
    ]