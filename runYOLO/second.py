import cv2
from ultralytics import YOLO
import cvzone

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


cap.set(3,1280)
cap.set(4,720)

while True:

    success, img = cap.read()

    #if img is not None:

    cv2.imshow("Image", img)
    cv2.waitKey(1)