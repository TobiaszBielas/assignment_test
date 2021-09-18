from.models import *
from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Sensor
        fields = '__all__'
        # depth = 2


class SensorConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = SensorConfiguration
        fields = '__all__'
        # depth = 1


class HandlerChoiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = HandlerChoice
        fields = '__all__'


class OutputChoiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = OutputChoice
        fields = '__all__'