from .serializers import *
from .models import *
from rest_framework import viewsets


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorConfigurationViewSet(viewsets.ModelViewSet):
    queryset = SensorConfiguration.objects.all()
    serializer_class = SensorConfigurationSerializer


class HandlerChoiceViewSet(viewsets.ModelViewSet):
    queryset = HandlerChoice.objects.all()
    serializer_class = HandlerChoiceSerializer


class OutputChoiceViewSet(viewsets.ModelViewSet):
    queryset = OutputChoice.objects.all()
    serializer_class = OutputChoiceSerializer