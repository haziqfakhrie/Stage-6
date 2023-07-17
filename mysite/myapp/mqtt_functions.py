import paho.mqtt.client as mqttclient
from django.http import HttpResponse
from .models import SensorData

from django.views.decorators.csrf import csrf_exempt


def on_connect(client, userdata, flags, rc):
    if rc== 0:
        print("Client is connected")
        client.subscribe("emqx/esp32")
    else:
        print("Client is not connected")

def on_message(client, userdata, message):
    print("Message Recieved: "+ str(message.payload.decode()))
    print('Topic: '+str(message.topic))
    data = str(message.payload.decode()).split(',')

    # Create a new SensorData instance and save it to the database
    sensor_data = SensorData(timestamp=data[0], waterlevel=float(data[1]))
    sensor_data.save()
    print("Data Saved!")  
@csrf_exempt
def subscribe_to_mqtt_broker(request):
    if request.method == "POST":
        # Handle the POST request, if needed
        pass

    return HttpResponse("Subscribed to MQTT broker")

connected = False
Messagerecieved = False
def subscribe():
    broker_address = "k3efbe9f.ala.us-east-1.emqxsl.com"
    port = 8883
    user = "test"
    password = "test1"

    client = mqttclient.Client(client_id="sloth_webapp")
    client.username_pw_set(user, password)

    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set()
    client.connect(broker_address, port)

    client.loop_forever()

