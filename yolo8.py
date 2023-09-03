from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredicor
import cv2
import threading
def model():
    model=YOLO("yolov8n-face.pt")
    return model
def results():
    mod=model()
    results=mod(source="0")
    frame=results[0].plot()
    cv2.imshow("frame",frame)
    frame.save("output.jpg")
    

if __name__== "__main__":
    p1=threading.Thread(target=model)
    p2 = threading.Thread(target=results)
   
    p1.start()
    p2.start()
    
