import cv2
import argparse
import threading
from ultralytics import YOLO
import supervision as sv
import numpy as np

model = YOLO("yolov8n-face.pt")
ZONE_POLYGON = np.array([
    [0, 0],
    [0.5, 0],
    [0.5, 1],
    [0, 1]
])
box_annotator = sv.BoxAnnotator(
        thickness=2, 
        text_thickness=2,
        text_scale=1
    )

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    global cap
    cap = cv2.VideoCapture()

    frame_width, frame_height = args.webcam_resolution

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    


    zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
    
    global zone
    zone = sv.PolygonZone(polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution))
    global zone_annotator 
    zone_annotator= sv.PolygonZoneAnnotator(
        zone=zone, 
        color=sv.Color.red(),
        thickness=2,
        text_thickness=4,
        text_scale=2
    )
def display():
    while True:
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )

        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)      
        
        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break


if __name__ == "__main__":
    p1=threading.Thread(target=main)
    p2 = threading.Thread(target=display)
    p1.start()
    p2.start()