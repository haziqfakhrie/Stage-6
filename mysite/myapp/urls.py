from django.urls import path

from . import views
from .views import (
    home_screen_view,
    subscribe_to_mqtt_broker,
)

urlpatterns = [

    path(' ', home_screen_view),
    path('mqtt/subscribe/', subscribe_to_mqtt_broker, name='subscribe'),

]