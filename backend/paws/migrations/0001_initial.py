# Generated by Django 2.1.7 on 2022-01-14 09:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceDescriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_Number', models.CharField(max_length=25)),
                ('manufacturer_Id', models.CharField(max_length=25)),
                ('model_Id', models.CharField(max_length=25)),
                ('ruleset_Ids', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('device_descriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.DeviceDescriptor')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceValidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isValid', models.BooleanField()),
                ('reason', models.CharField(max_length=150)),
                ('deviceDesc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.DeviceDescriptor')),
            ],
        ),
        migrations.CreateModel(
            name='EventTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_Time', models.DateTimeField()),
                ('stop_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('channels', models.IntegerField(primary_key=True, serialize=False)),
                ('frequency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FrequencyRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_Hz', models.FloatField()),
                ('stop_Hz', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('dane_code', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Departamento')),
            ],
            options={
                'verbose_name': 'Geolocation',
                'verbose_name_plural': 'Geolocations',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='RulsetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=50)),
                ('rulsetId', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spectrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=50)),
                ('channels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Frequency')),
                ('geolocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Geolocation')),
            ],
        ),
        migrations.CreateModel(
            name='SpectrumSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.EventTime')),
                ('spectrum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Spectrum')),
            ],
        ),
        migrations.CreateModel(
            name='SpectrumSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency_Ranges', django.contrib.postgres.fields.jsonb.JSONField(encoder='')),
                ('needs_Spectrum_Report', models.BooleanField()),
                ('max_Total_BwHz', models.FloatField(blank=True)),
                ('max_Contiguous_Bw_Hz', models.FloatField(blank=True)),
                ('geolocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Geolocation')),
                ('rulset_Info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.RulsetInfo')),
                ('spectrum_Schedules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.SpectrumSchedule')),
                ('time_Range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.EventTime')),
            ],
        ),
        migrations.AddField(
            model_name='devicedescriptor',
            name='device_capabilities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.FrequencyRange'),
        ),
        migrations.AddField(
            model_name='devicedescriptor',
            name='geolocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws.Geolocation'),
        ),
    ]
