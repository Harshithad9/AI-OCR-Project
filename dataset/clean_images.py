import os
import cv2
from tqdm import tqdm

# Path to your dataset
base_path = "dataset/Aadhar-card-entity-detection-1"
subfolders = ["train", "valid", "test"]

def is_image_corrupted(image_path):
    """Check if an image can be opened successfully."""
    try:
        img = cv2.imread(image_path)
        if img is None or img.size == 0:
            return True
        return False
    except Exception:
        return True

def remove_duplicate_and_corrupted():
    for subfolder in subfolders:
        images_path = os.path.join(base_path, subfolder, "images")
        cleaned = 0
        if not os.path.exists(images_path):
            continue

        print(f"\n🔍 Checking {subfolder} images...")
        seen_hashes = set()

        for filename in tqdm(os.listdir(images_path)):
            file_path = os.path.join(images_path, filename)

            # Skip non-image files
            if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            # Check for corruption
            if is_image_corrupted(file_path):
                os.remove(file_path)
                cleaned += 1
                continue

            # Check for duplicates
            try:
                img = cv2.imread(file_path)
                img_hash = hash(img.tobytes())
                if img_hash in seen_hashes:
                    os.remove(file_path)
                    cleaned += 1
                else:
                    seen_hashes.add(img_hash)
            except Exception:
                continue

        print(f"✅ {subfolder}: {cleaned} duplicate/corrupted images removed.")

if __name__ == "__main__":
    remove_duplicate_and_corrupted()
    print("\n🎉 Image cleaning completed successfully!")
