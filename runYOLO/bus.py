import cv2
from ultralytics import YOLO
model = YOLO('yolov8l.pt')

results = model('road.mp4', show=True)
results = model('D:\\pythonProject\\object-detection-YOLO\\runYOLO\\road.mp4', show=True)
if(results):
    cv2.waitKey(1)