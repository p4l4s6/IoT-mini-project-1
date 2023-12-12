import json

import paho.mqtt.client as mqtt

# MQTT settings
mqtt_broker_address = "16.170.238.248"
mqtt_port = 1886
mqtt_topic = "device_1"

# Initialize MQTT client
client = mqtt.Client()


# Callback when connected to MQTT broker
def on_connect(cl, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    cl.subscribe(mqtt_topic)


# Callback when a message is received from the subscribed topic
def on_message(cl, userdata, msg):
    try:
        # Decode JSON data
        json_data = json.loads(msg.payload.decode("utf-8"))
        temp = json_data.get("temp")
        pressure = json_data.get("pressure")
        print(f"Temperature: {temp} \n Pressure: {pressure}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


# Set MQTT callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker_address, mqtt_port, 60)

# Start the MQTT loop
client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the MQTT broker
client.disconnect()
