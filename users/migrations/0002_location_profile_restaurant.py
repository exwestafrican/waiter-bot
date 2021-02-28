# Generated by Django 3.1.7 on 2021-02-28 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('area', models.CharField(help_text='locations are usually generic, like mainland or Ota', max_length=800, null=True)),
                ('state', models.CharField(help_text='lagos state', max_length=600)),
                ('popular_name', models.CharField(help_text='where do people usually attribute this place to', max_length=800, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(help_text='is this measured in scopes, or boxes or bottles', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='restaurant name', max_length=500)),
                ('code', models.CharField(blank=True, max_length=4, null=True, unique=True)),
                ('in_school', models.BooleanField(default=True)),
                ('address', models.OneToOneField(blank=True, help_text='where is your restaurant located', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('available_in', models.ManyToManyField(help_text='where are the places this restruant is located in', related_name='available_in', to='users.Location')),
                ('owner', models.ForeignKey(help_text='who owns this restaurant', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]