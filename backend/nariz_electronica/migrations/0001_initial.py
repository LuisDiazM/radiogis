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
            name='Analisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('tiempo_medicion_segundos', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DatosEvaluar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicion', django.contrib.postgres.fields.jsonb.JSONField(encoder='')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicion', django.contrib.postgres.fields.jsonb.JSONField(encoder='')),
                ('analisis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nariz_electronica.Analisis')),
            ],
        ),
        migrations.AddField(
            model_name='analisis',
            name='entrenamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nariz_electronica.Entrenamiento'),
        ),
    ]
