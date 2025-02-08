import cv2
import numpy as np

haar_file = 'C:/Users/feroz/OneDrive/Desktop/Web Dev/Computer Vision/Face-Detection/haarcascade_frontalface_default.xml'  # Keep your Haar cascade path

face_cascade = cv2.CascadeClassifier(haar_file)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read() 

    if not ret:
        print("Error reading frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  

    cv2.imshow('Webcam Face Detection', frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release() 
cv2.destroyAllWindows()  