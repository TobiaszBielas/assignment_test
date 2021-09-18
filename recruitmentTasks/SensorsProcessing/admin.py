from django.contrib import admin
from .models import *


admin.site.register(SensorConfiguration)
admin.site.register(Sensor)
admin.site.register(HandlerChoice)
admin.site.register(OutputChoice)