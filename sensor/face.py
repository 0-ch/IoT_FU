from time import sleep
from gpiozero import MotionSensor, LED, DistanceSensor, CPUTemperature
import Adafruit_DHT
import os
import cv2
import vlc
import tensorflow as tf
import pickle
import mtcnn
def get_face_embedding(facenet,face_image):
    face_image = (face_image-tf.math.reduce_mean(face_image))/tf.math.reduce_std(face_image)
    embedding = facenet.predict(face_image[tf.newaxis,:])
    embedding = embedding/tf.norm(embedding)
    return embedding

detector = mtcnn.MTCNN()
cmodel = tf.keras.models.load_model('face_model.h5', compile=False)
print("load face_model finish")
facenet = tf.keras.models.load_model('facenet_model.h5', compile=False)
print("load facenet_model finish")
with open('face_model.pickle','rb') as f:
    cmodel.person_name = pickle.load(f)
threshold = 1/len(cmodel.person_name)*1.75
pir = MotionSensor(22)
dist_sensor = DistanceSensor(echo = 24,trigger = 23,max_distance = 2, threshold_distance=0.1)

while True:
    if pir.motion_detected:
        print("get PIR signal")
        distance_cm = dist_sensor.distance * 100
        if distance_cm < 80:
            flag = False
            print(distance_cm,"cm")
            os.system("fswebcam image.jpg")
            sleep(5)
            x_img = tf.keras.preprocessing.image.img_to_array(tf.keras.preprocessing.image.load_img("image.jpg"))
            results = detector.detect_faces(x_img)
            print(results)
            if len(results)>0:
                for result in results:
                    x1, y1, width, height = result['box']
                    x1, y1 = abs(x1), abs(y1)
                    x2, y2 = x1 + width, y1 + height 
                    face = tf.image.resize(x_img[y1:y2,x1:x2],(160,160)) 
                    embedding = get_face_embedding(facenet,face)
                    prob      = cmodel.predict(embedding)
                    print("prob:",prob)
                    name      = cmodel.person_name[tf.math.argmax(prob,axis=1).numpy()[0]]    
                    print("name:",name)
                    if prob[0][tf.math.argmax(prob,axis=1).numpy()[0]]>threshold:
                        flag = True
                        print("!OPEN DOOR!")
            else:
                print("no face")
            sleep(0.7)
        sleep(1)
    sleep(1.5)