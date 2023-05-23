import paho.mqtt.client as mqtt

# MQTT broker settings
broker = "localhost"
port = 1883
topic="mytopic"

# Connect to the MQTT broker
client = mqtt.Client()
client.connect(broker, port)

# Publish a message

topic = input("enter the topic:")
while True:
    message = input("connected  (or 'q' to quit): ")

    if message.lower() == 'q':
        break
    client.publish(topic, message)

# Disconnect from the broker
client.disconnect()

