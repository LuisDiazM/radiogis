# Generated by Django 2.1.7 on 2022-01-14 09:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variables', django.contrib.postgres.fields.jsonb.JSONField()),
                ('fecha', models.DateTimeField(blank=True)),
            ],
        ),
    ]
