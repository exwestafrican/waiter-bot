# Generated by Django 3.1.7 on 2021-02-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0002_auto_20210227_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='short_description',
            field=models.CharField(default='', help_text='give a brief description of what this does', max_length=500),
        ),
    ]
