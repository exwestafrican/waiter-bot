# Generated by Django 3.1.7 on 2021-02-28 14:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0002_auto_20210228_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='is this measured in scopes, or boxes or bottles', max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('base_charge', models.DecimalField(decimal_places=2, help_text='how much does one unit of this cost', max_digits=9)),
                ('addition_charge', models.DecimalField(decimal_places=2, help_text='how much does every additional unit charge', max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('countable', models.BooleanField(default=True)),
                ('measured_in', models.ForeignKey(blank=True, help_text='is this measured in scopes, or boxes or bottles', null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.measurementtype')),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
