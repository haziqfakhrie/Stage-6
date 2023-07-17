from django.shortcuts import render
from . import mqtt_functions

import threading


from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("Welcome to Stupendous Sloths")

def home_screen_view(request):
    print(request.headers)
    return render(request, "base.html",{})
def start_mqtt_subscription():
    # Call the MQTT subscription function
    mqtt_functions.subscribe()
def subscribe_to_mqtt_broker(request):
    mqtt_thread = threading.Thread(target=start_mqtt_subscription)
    mqtt_thread.start()


    return HttpResponse("Subscribed to MQTT Broker")

