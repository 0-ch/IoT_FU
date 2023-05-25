from time import sleep
from gpiozero import MotionSensor, LED, DistanceSensor, CPUTemperature
import Adafruit_DHT
import os
import cv2
import vlc

pir = MotionSensor(22)
sound = vlc.MediaPlayer("demo.mp3")
crawler_flag = True
while True :
    if pir.motion_detected:
        print("get PIR signal")
        if crawler_flag:
            print("umbrella remember")
            sound.play()
            sleep(2)
            sound.stop()
        else:
            h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
            print("humidty is {} %".format(h))
            print("temperature is {} °C".format(t))
            if h > 65 :
                print("umbrella remember")
                sound.play()
                sleep(2)
                sound.stop()
    sleep(1)


"""
detect face
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
"""

"""
#PIR func
pir = MotionSensor(22)
while True:
    if pir.motion_detected:
        print("get signal")
    else:
        print("no")
    sleep(1.5)

#camera func
while True :
    os.system("fswebcam image.jpg")
    image = cv2.imread("image.jpg")
    cv2.namedWindow("demo", cv2.WINDOW_NORMAL)
    cv2.imshow("demo", image)
    sleep(0.7)

#distance sensor func
dist_sensor = DistanceSensor(echo = 24,trigger = 23,max_distance = 2, threshold_distance=0.1)

while True:
    distance_cm = dist_sensor.distance * 100
    print(distance_cm)
    sleep(1)

#dht sensor func
while True:
    h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
    print("humidty is {} %".format(h))
    print("temperature is {} °C".format(t))
    sleep(1)
"""