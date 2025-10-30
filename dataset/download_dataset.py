from roboflow import Roboflow

# Initialize with your Roboflow API key
rf = Roboflow(api_key="q5cPHjORj7zUhTGlqYeu")

# Access the Aadhaar dataset
project = rf.workspace("jizo").project("aadhar-card-entity-detection")

# Download version 1 in YOLOv8 format (you can also try 'coco' or 'voc')
dataset = project.version(1).download("yolov8")

print("✅ Dataset downloaded successfully!")
