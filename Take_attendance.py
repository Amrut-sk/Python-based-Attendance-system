# -*- coding: utf-8 -*-

import cv2
import csv  
from csv import writer
import pandas as pd

fields = ['S.no', 'Name', 'Attendance'] 
filename = "Attendance_records.csv" 

 
def write_attendance(filename,fields):
    with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
        csvwriter.writerow(fields)  

write_attendance(filename,fields)
        


def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
    coords = []
    for(x, y, w, h) in features:        
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        id,_ = clf.predict(gray_img[x:x+w, y:y+h])
        if id == 1:
            s = id
            #cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            cv2.putText(img, "AMRUT", (x+30, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            coords = [x, y, w, h]
            rows=[s, 'Amrut', 'Present']
            append_row(filename, rows)
                                    
        if id == 2:
            s = id
            #cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            cv2.putText(img, "ANANT", (x+30, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            coords = [x, y, w, h]    
            rows=[s, 'Anant', 'Present']
            append_row(filename, rows)    
                                      
        

def append_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def recognize(img, clf, faceCascade):
    color = {"blue":(255,0,0),"red":(0,0,255),"green":(0,255,0),"orange":(100,128,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color["orange"], "Face", clf)
    return img

        

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")

video_capture = cv2.VideoCapture(0)


while True:
    _, img = video_capture.read()
    #img = detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade, img_id)
    img = recognize(img, clf, faceCascade)
    cv2.imshow("Face Detection (Enter q to EXIT !!!)",img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
    
video_capture.release()
cv2.destroyAllWindows()
