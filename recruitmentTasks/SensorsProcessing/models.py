from django.db import models
from django.db.models.fields import AutoField, BooleanField, CharField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.contrib.postgres.fields import ArrayField


class SensorConfiguration(models.Model):
    # DEFAULT_CHOICE = ('N', "nothing")
    # HANDLERS_CHOICE = (
    #     DEFAULT_CHOICE,
    #     ('Trim', "trim"),
    #     ('PTM', "pad to multiple"),
    #     ('Timestamp', "time stamp")
    # )
    # OUTPUT_CHOICE = (
    #     DEFAULT_CHOICE,
    #     ('Console', "console"),
    #     ('File', 'file')
    # )
    sensor_model = CharField(max_length=32, unique=True)
    handler = ManyToManyField('HandlerChoice', related_name='handler')
    output = ManyToManyField('OutputChoice', related_name='output')
    # handler = ArrayField(CharField(choices=HANDLERS_CHOICE, blank=True, default=DEFAULT_CHOICE, max_length=32),)
    # output = ArrayField(CharField(choices=OUTPUT_CHOICE, blank=True, default=DEFAULT_CHOICE, max_length=32),)

    def __str__(self):
        return self.sensor_model


class Sensor(models.Model):
    sensor_id = AutoField(primary_key=True)
    model = ForeignKey(SensorConfiguration, on_delete=models.CASCADE, db_column='SensorConfiguration.sensor_model', related_name="sensors", null=False)
    payload = CharField(max_length=64)
    completed = BooleanField(default=False)
    
    def __str__(self):
        return str(self.model)


class OutputChoice(models.Model):
    name = CharField(null=False, max_length=32)

    def  __str__(self):
        return self.name


class HandlerChoice(models.Model):
    name = CharField(null=False, max_length=32)
    description = TextField(null=True)

    def  __str__(self):
        return self.name