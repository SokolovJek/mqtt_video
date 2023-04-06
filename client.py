# Importing Libraries
import cv2 as cv
import paho.mqtt.client as mqtt
import base64
import time


username = 'name'
password = 'pas'

# Raspberry PI IP address
MQTT_BROKER = "192.168.155.48"
# MQTT_BROKER = "172.25.112.1"

# Topic on which frame will be published
MQTT_SEND = "home/server"
# Object to capture the frames
cap = cv.VideoCapture(4)
# Phao-MQTT Clinet
client = mqtt.Client()
client.username_pw_set(username, password)
# Establishing Connection with the Broker
client.connect(MQTT_BROKER, port=8883)
try:
    while True:
        start = time.time()
        time.sleep(2)
        # Read Frame
        _, frame = cap.read()
        # Encoding the Frame
        _, buffer = cv.imencode('.jpg', frame)
        # Converting into encoded bytes
        jpg_as_text = base64.b64encode(buffer)
        # Publishig the Frame on the Topic home/server
        client.publish(MQTT_SEND, jpg_as_text)
        end = time.time()
        t = end - start
        fps = 1/t
        print(fps)
except:
    cap.release()
    client.disconnect()
    print("\nNow you can restart fresh")
