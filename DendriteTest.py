from ultralytics import YOLO

# ========================================
# Step 1: Define paths to your dataset YAML and test image
# ========================================
data_yaml = "C:/Users/river/488/Dendtritic_Identifiers.yaml"  # Update with the path to your YAML file
test_image = "C:/Users/river/OneDrive/Documents/#EEE488/DendriteImages/Dendrite3.jpg"               # Update with a test image path

# ========================================
# Step 2: Load a pre-trained YOLOv8 model
# ========================================
model = YOLO("yolov8n.pt")  # You can change to yolov8s.pt, yolov8m.pt, etc. if needed

# ========================================
# Step 3: Train the model on your dataset
# ========================================
train_results = model.train(
    data=data_yaml,
    epochs=100,                 # Adjust the number of epochs as needed
    imgsz=768,                  # Image size used for training
    project="dendritic_identifiers_project",  # Folder where training results are saved
    name="yolov8n_dendritic"    # Name for this training run
)

# ========================================
# Step 4: Validate the model on the validation split
# ========================================
val_results = model.val(data=data_yaml)

# ========================================
# Step 5: Test the trained model on a sample image
# ========================================
results = model(test_image)

# Show the test image with predictions
results[0].show()

# Print the detected objects: class names and bounding boxes
for result in results:
    print("Detected classes:", result[0].names)
    print("Bounding boxes:", result[0].boxes)