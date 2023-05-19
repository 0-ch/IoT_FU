from time import sleep
from gpiozero import MotionSensor, LED, DistanceSensor, CPUTemperature
import Adafruit_DHT
import os
import cv2
import vlc

pir = MotionSensor(22)
dist_sensor = DistanceSensor(echo = 24,trigger = 23,max_distance = 2, threshold_distance=0.1)

while True:
    if pir.motion_detected:
        print("get PIR signal")
        distance_cm = dist_sensor.distance * 100
        if distance_cm < 80:
            print(distance_cm,"cm")
            os.system("fswebcam image.jpg")
            sleep(0.7)
        sleep(1)
    sleep(1.5)