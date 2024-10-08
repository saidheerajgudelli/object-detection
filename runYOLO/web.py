import cv2
from ultralytics import YOLO
import cvzone
import math

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3,1280)
cap.set(4,720)

model = YOLO('yolov8l.pt')

while True:

    success, img = cap.read()
    results = model(img,stream=True)

    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #print(x1,y1,x2,y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img,(x1,y1,w,h))

            conf = math.ceil(box.conf[0]*100)/100
            print(conf)
            cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(35,y1)),2,2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    #if img is not None:

