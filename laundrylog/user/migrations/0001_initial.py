# Generated by Django 3.0.8 on 2020-07-17 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=191, null=True)),
                ('email', models.CharField(max_length=191, null=True, unique=True)),
                ('password', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
