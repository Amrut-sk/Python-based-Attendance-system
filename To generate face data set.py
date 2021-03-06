# -*- coding: utf-8 -*-

import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)  ## proper folder name data2/...
    
    
def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
    coords = []
    for(x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            
        coords = [x, y, w, h]
        
    return coords


def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade, img_id):
    color = {"blue":(255,0,0),"red":(0,0,255),"green":(0,255,0),"white":(255,255,255)}
    
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")
    
    if len(coords)==4:
        roi_img = img[coords[0]:coords[0]+coords[2], coords[1]:coords[1]+coords[3]]
        
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)
        
        
        # coords = draw_boundary(roi_img, eyeCascade, 1.1, 14, color['red'], "Eyes")
        # coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'], "Mouth")
        # coords = draw_boundary(roi_img, noseCascade, 1.1, 12, color['green'], "Nose")
    return img
 

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
noseCascade = cv2.CascadeClassifier("Nose.xml")
mouthCascade = cv2.CascadeClassifier("Mouth.xml") 


video_capture = cv2.VideoCapture(0)

img_id = 0

while True:
    _, img = video_capture.read()
    img = detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade,img_id)    
    cv2.imshow("Face Detection",img)
    img_id +=1
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()