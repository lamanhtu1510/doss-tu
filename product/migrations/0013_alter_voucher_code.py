# Generated by Django 3.2.5 on 2021-07-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]