from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from SensorsProcessing.views import *


router = DefaultRouter()
router.register(r'sensor', SensorViewSet)
router.register(r'configuration', SensorConfigurationViewSet)
router.register(r'handler', HandlerChoiceViewSet)
router.register(r'output', OutputChoiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(router.urls)),

]
