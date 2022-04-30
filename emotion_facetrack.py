import numpy as np
import cv2
import os
import time
from pwmdrive import PWMDrive
from rgbhappy import RGBHappy
from tensorflow.keras import Sequential #for emotion recognition
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


class Facetrack():

    # Constructor
    def __init__(self):
        self.start = time.time()
    
        # Settings
        self.width = 640
        self.height = 480
        #self.maxspeed = 1250
        self.maxspeed = 2000
        self.rangemin = int(self.width/2*0.7)
        self.rangemax = int(self.width/2*1.3)

        # Initialize motors
        self.pwm = PWMDrive()
        self.pwm.stop()
        
        # Initialize RGB matrix
        self.rgb = RGBHappy()
        self.rgb.q()

        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        
        # Initialize face and emotion recognition 
        self.classifier = load_model('ferjj.h5') # This model has a set of 6 classes
        self.class_labels = {0: 'Angry', 1: 'Fear', 2: 'Happy', 3: 'Neutral', 4: 'Sad', 5: 'Surprise'}
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
        self.last_emo = ""
        self.detections = 0


    # Detects face from given still image (can detect multiple but returns only one)
    def face_detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)        
        if faces is (): 
            return None, None, None, None, None
        #print(len(faces), "faces detected: ", faces)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        return x, w, y, h, roi_gray


    # Detects emotions from given face
    def emotion_detect(self, face):              
        roi = face.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        preds = self.classifier.predict(roi)[0]
        label = self.class_labels[preds.argmax()]
        if (self.last_emo == label):
            self.detections += 1
        else:
            self.detections = 1
        self.last_emo = label 
        print(label, self.detections, "detections")
        if self.detections == 2:
            if label == "Angry": self.rgb.angry()
            elif label == "Fear": self.rgb.fear()
            elif label == "Happy": self.rgb.happy()
            elif label == "Neutral": self.rgb.neutral()
            elif label == "Sad": self.rgb.sad()
            elif label == "Surprise": self.rgb.surprise()
 
 
    def facetrack(self):
        print("Searching...")        
        
        while True:
        
            # Terminate after 3:55
            if time.time() - self.start > 235:
                print("Done!")
                self.pwm.stop()
                self.rgb.blank()
                break
        
            # Get still image from camera
            ret, img = self.cap.read()
            
            x, w, y, h, face = self.face_detect(img)
            if face is None: 
                #self.pwm.stop()
                continue
            
            # Detect emotion from / rotate towards face
            if x in range(self.rangemin, self.rangemax):
                print("Face in range", self.rangemin, self.rangemax, ": ", x)
                self.pwm.stop()
                self.emotion_detect(face)
                #time.sleep(1)
                #self.rgb.q()
            elif x > self.rangemax:
                print("Face at right: ", x)                                
                #angle = int((x-self.width/2)/(self.width/2)*39)
                #self.pwm.cw(angle, 1000)                
                speed = int((x-self.width/2)/(self.width/2)*self.maxspeed)
                self.pwm.drive(0, 0, speed, speed)
            elif x < self.rangemin:
                print("Face at left: ", x)
                #angle = int((self.width/2-x)/(self.width/2)*39)
                #self.pwm.ccw(angle, 1000)                
                speed = int((self.width/2-x)/(self.width/2)*self.maxspeed)
                self.pwm.drive(1, 1, speed, speed)

    
    def stop(self):
        self.pwm.stop()
    
    
if __name__ == "__main__":
    ft = Facetrack()
    try:
        input("Press Enter to start...")
        ft.facetrack()
    except Exception as e:
        print(e)
    finally:
        ft.stop()
        