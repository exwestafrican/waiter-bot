# Generated by Django 3.1.7 on 2021-03-06 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cart_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='reference',
            new_name='payment_link',
        ),
    ]
