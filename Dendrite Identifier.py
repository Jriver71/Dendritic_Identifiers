from ultralytics import YOLO

# Load the best-trained model weights
model = YOLO("C:/Users/river/dendritic_identifiers_project/yolov8n_dendritic20/weights/best.pt")

# Now 'model' knows about dendrite structures learned during training
results = model("C:/Users/river/488/NewDendrites/0.jpg")
results[0].show()