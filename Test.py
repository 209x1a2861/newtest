import cv2  
import numpy as np  
import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "lbpcascade_frontalface.xml"
)

cap = cv2.VideoCapture("rtsp://admin:admin@192.168.0.113:1935") 
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
while(True):
    
    # Capture image frame-by-frame  
    ret, frame = cap.read()  
    if not ret:
        break
    
    faces=detect_bounding_box(frame)
  
    
    # Our operations on the frame come here  
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # Display the resulting frame  
    cv2.imshow('RTSP',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break 
# When everything done, release the capture  
cap.release()  
cv2.destroyAllWindows()  
