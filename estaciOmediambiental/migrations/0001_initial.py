# Generated by Django 3.1.7 on 2021-02-23 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.TextField(verbose_name='')),
                ('estatic', models.BooleanField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Registre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(auto_now=True, verbose_name='')),
                ('valor', models.TextField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.TextField(verbose_name='')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estaciOmediambiental.client', verbose_name='')),
            ],
        ),
    ]
