from mtcnn import MTCNN
import cv2
import queue
import threading
detector = MTCNN()
#Load a videopip TensorFlow
q=queue.Queue()

video_capture = cv2.VideoCapture(0)

def capt():
    print("start streaming")
    
    while (True):
        ret, frame = video_capture.read()
        q.put(frame)
        if q.empty()!=True:
            frame=q.get()
            boxes = detector.detect_faces(frame)
            if boxes:
 
                box = boxes[0]['box']
                conf = boxes[0]['confidence']
                x, y, w, h = box[0], box[1], box[2], box[3]
 
                if conf > 0.5:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
            cv2.imshow("Frame", frame)
        # frame = cv2.resize(frame, (600, 400))
def display():
    while True:
        if q.empty()!=True:
            frame=q.get()
            print("hiii")
            cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
    video_capture.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    p1=threading.Thread(target=capt)
    p2 = threading.Thread(target=display)
    p1.start()
    p2.start()