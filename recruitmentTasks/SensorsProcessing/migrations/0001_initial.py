# Generated by Django 3.2.7 on 2021-09-18 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandlerChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutputChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SensorConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_model', models.CharField(max_length=32, unique=True)),
                ('handler', models.ManyToManyField(related_name='handler', to='SensorsProcessing.HandlerChoice')),
                ('output', models.ManyToManyField(related_name='output', to='SensorsProcessing.OutputChoice')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensor_id', models.AutoField(primary_key=True, serialize=False)),
                ('payload', models.CharField(max_length=64)),
                ('completed', models.BooleanField(default=False)),
                ('model', models.ForeignKey(db_column='SensorConfiguration.sensor_model', on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='SensorsProcessing.sensorconfiguration')),
            ],
        ),
    ]
