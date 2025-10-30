import os
import json

# Paths
dataset_path = "dataset/Aadhar-card-entity-detection-1/augmented/train"
images_dir = os.path.join(dataset_path, "images")
labels_dir = os.path.join(dataset_path, "labels")

# Output JSON file
output_json = os.path.join(dataset_path, "formatted_labels.json")

# Define label names (update if your dataset has different ones)
label_map = {
    0: "Name",
    1: "DOB",
    2: "Gender",
    3: "AadhaarNumber",
    4: "Address"
}

data = []

# Iterate over all label files
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):
        image_name = label_file.replace(".txt", ".jpg")
        image_path = os.path.join(images_dir, image_name)

        with open(os.path.join(labels_dir, label_file), "r") as f:
            lines = f.readlines()

        entities = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 5:
                cls, x, y, w, h = parts
                entities.append({
                    "label": label_map.get(int(cls), "Unknown"),
                    "x_center": float(x),
                    "y_center": float(y),
                    "width": float(w),
                    "height": float(h)
                })

        if entities:
            data.append({
                "image": image_name,
                "entities": entities
            })

# Save to JSON file
with open(output_json, "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ Labels formatted and saved to {output_json}")
