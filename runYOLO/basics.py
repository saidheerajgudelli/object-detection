import cv2
from ultralytics import YOLO
import cvzone

cap=cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

#model=YOLO('../venv')
while True:
    if img is not None:
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        success, img = cap.read()
        print("Frame captured successfully:", success)
