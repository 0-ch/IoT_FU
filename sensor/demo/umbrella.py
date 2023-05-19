from time import sleep
from gpiozero import MotionSensor, LED, DistanceSensor, CPUTemperature
import Adafruit_DHT
import os
import cv2
import vlc

pir = MotionSensor(22)
sound = vlc.MediaPlayer("demo.mp3")
while True :
    if pir.motion_detected:
        print("get PIR signal")
        h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
        print("humidty is {} %".format(h))
        print("temperature is {} °C".format(t))
        crawler_flag =False
        f = open("test.txt","r")
        if f.readlines()[0].find("False") == -1:
            crawler_flag = True
        if crawler_flag or h > 75:
            print("umbrella remember")
            sound.play()
            sleep(2)
            sound.stop()
    sleep(1)