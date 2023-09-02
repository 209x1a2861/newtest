from PIL import Image
from ultralytics import YOLO
import cv2
import torch
print(torch.__version__, torch.cuda.is_available())


model = YOLO('yolov8n-face.pt')
model.export(format="onnx")
results = model.predict(source="0",conf=0.5,show=True)  # results list
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()
