import os
import cv2
import albumentations as A
from tqdm import tqdm
import shutil

# Define paths
BASE_DIR = "dataset/Aadhar-card-entity-detection-1"
OUTPUT_DIR = os.path.join(BASE_DIR, "augmented")

# Create output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Augmentation pipeline (you can tweak this later)
transform = A.Compose([
    A.Rotate(limit=15, p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.HorizontalFlip(p=0.3),
    A.RandomScale(scale_limit=0.1, p=0.3),
])

def augment_images(subset="train"):
    input_path = os.path.join(BASE_DIR, subset, "images")
    label_path = os.path.join(BASE_DIR, subset, "labels")
    output_images_path = os.path.join(OUTPUT_DIR, subset, "images")
    output_labels_path = os.path.join(OUTPUT_DIR, subset, "labels")

    os.makedirs(output_images_path, exist_ok=True)
    os.makedirs(output_labels_path, exist_ok=True)

    for img_name in tqdm(os.listdir(input_path)):
        if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(input_path, img_name)
        label_file = img_name.rsplit(".", 1)[0] + ".txt"
        label_path_file = os.path.join(label_path, label_file)

        # Skip if label doesn't exist
        if not os.path.exists(label_path_file):
            continue

        # Read image
        image = cv2.imread(img_path)
        if image is None:
            continue

        # Perform augmentation
        augmented = transform(image=image)
        aug_image = augmented["image"]

        # Save augmented image and label
        new_image_name = "aug_" + img_name
        cv2.imwrite(os.path.join(output_images_path, new_image_name), aug_image)
        shutil.copy(label_path_file, os.path.join(output_labels_path, "aug_" + label_file))

    print(f"✅ Augmented {subset} dataset saved at {output_images_path}")

if __name__ == "__main__":
    augment_images("train")
    print("\n🎉 Data augmentation completed successfully!")
