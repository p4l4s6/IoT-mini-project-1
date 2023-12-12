import json
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
from collections import deque

# MQTT settings
mqtt_broker_address = "16.170.238.248"
mqtt_port = 1886
mqtt_topic = "device_one"

# Initialize MQTT client
client = mqtt.Client()

# Data storage for the live chart
max_data_points = 10
temp_data = deque(maxlen=max_data_points)
pressure_data = deque(maxlen=max_data_points)

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

# Callback when a message is received from the subscribed topic
def on_message(client, userdata, msg):
    try:
        # Decode JSON data
        data = json.loads(msg.payload.decode("utf-8"))
        temp = data.get("temp")
        pressure = data.get("pressure")

        # Update live chart data
        temp_data.append(temp)
        pressure_data.append(pressure)

        # Update and redraw the live chart
        update_chart()

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

# Function to update and redraw the live chart
def update_chart():
    plt.clf()
    plt.plot(temp_data, label="Temperature")
    plt.plot(pressure_data, label="Pressure")
    plt.xlabel("Data Points")
    plt.ylabel("Values")
    plt.legend()
    plt.draw()
    plt.pause(0.1)

# Set MQTT callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker_address, mqtt_port, 60)

# Initialize the live chart
plt.ion()  # Turn on interactive mode for live updating
plt.figure()

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
