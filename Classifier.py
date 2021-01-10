

import os, cv2
import numpy as np
from PIL import Image

def train_classifier(data_dir):
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []
    
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        ida = int(os.path.split(image)[1].split(".")[1])
        
        faces.append(imageNp)
        ids.append(ida)
        
    ids = np.array(ids)
    
    
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.yml")
    
    
train_classifier("data")