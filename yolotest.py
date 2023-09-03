import cv2
from ultralytics import YOLO
import subprocess
import requests
import json
import random
import base64
from PIL import Image
import threading

import torch
cap=cv2.VideoCapture(0)
model=YOLO("yolov8n-face.pt")
def show_frame(frame):
    
    cv2.imshow("face detection",frame)
while cap.isOpened():
    success,frame=cap.read()
    if success:
    # Run YOLOv8 inference on the frame
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imwrite("test1.jpeg", annotated_frame)
    # Encode the resized annotated frame to base64


    # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        show_frame(annotated_frame)
    # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break    
    else:
        break
    
    

cap.release()
cap.destroyAllWindows()