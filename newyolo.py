import cv2
from ultralytics import YOLO
import supervision as sv
import numpy as np
import subprocess
from multiprocessing import Process
import time
import gc
import PIL
import os
global count

def beep():
    subprocess.call(["afplay", "/System/Library/Sounds/Glass.aiff"])

def detect_objects(model, video_source,name,count):
         
        
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
)
    fps_start_time = time.time()
    fps=0
    start_time = time.time() # variable to keep track of time
    for result in model.predict(source=video_source,
                        device="cpu",
                        #cache=False,
                        # save=False,
                        # visualize=False,
                        
                        # max_det=10,
                        stream=True,
                        # imgsz=320,
                        agnostic_nms=True):
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)
        for coordinates in detections:
            if video_source=="0":
                if coordinates[2]>0.60:
                    count+=1
                    (x,y,w,h)=coordinates[0].astype('int')
                    image=frame[y:h,x:w]
                    print(x,y,h,w)
                    di=r"C:\Users\bharg\OneDrive\Desktop\practice\faces"
                    os.chdir(di)
                    if name not in os.listdir():
                        os.mkdir(name)
                    path=os.getcwd()
                    path=path+"\\"+name
                    os.chdir(path)
                    status=cv2.imwrite(name+"("+str(count)+")"+".jpg",image)
                if count>30:
                    return
            else:
                if coordinates[2]>0.40:
                    (x,y,w,h)=coordinates[0].astype('int')
                    
                    image=frame[y:h,x:w]
                    print(x,y,h,w)

                    cv2.imwrite("reco.jpg",image)
                
        fps_end_time = time.time()
        fps_diff_time = fps_end_time - fps_start_time
        fps = 1 / fps_diff_time
        fps_start_time = fps_end_time
        fps_text="INFERENCE-FPS:{:.0f}".format(fps)
        cv2.putText(frame, fps_text, (5,30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        
        frame = box_annotator.annotate(
        scene=frame, 
        detections=detections
        )
        print(count)
        cv2.imshow(name, frame)

        if (cv2.waitKey(30) == 27):
            break
    
    # release memory every two minutes
        if time.time() - start_time >120:
            print(f"Release memory for {video_source}")
            beep()
            del result
            del frame
            del detections
            gc.collect()
            del fps_text
            start_time = time.time()
    cv2.destroyAllWindows()

def main():
# list of video sources
    video_sources = list(map(str,input("enter sources: ").split()))
    count=0

    model = YOLO("yolov8n-face.pt")
    processes = []
    for video_source in video_sources:
        if video_source=="0":
            name=input("enter person name and look at webcam : ")
            p = Process(target=detect_objects, args=(model, video_source,name,count))
            p.start()
            processes.append(p)
        else:
            p = Process(target=detect_objects, args=(model, video_source,"normal detection"))
            p.start()
            processes.append(p)
            
    for p in processes:
        if not p.is_alive():
            p.join()
            processes.remove(p)

if __name__ == "__main__":
    main()
