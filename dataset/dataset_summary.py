import os

# Root path for your dataset
dataset_root = "dataset/Aadhar-card-entity-detection-1"

# Output summary file
summary_file = os.path.join(dataset_root, "dataset_summary.txt")

def count_files(path):
    """Return total image and label counts in the given path"""
    image_dir = os.path.join(path, "images")
    label_dir = os.path.join(path, "labels")

    if not os.path.exists(image_dir) or not os.path.exists(label_dir):
        return (0, 0, 0)

    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    missing_labels = [img for img in image_files if img.replace('.jpg', '.txt') not in label_files]
    missing_images = [lbl for lbl in label_files if lbl.replace('.txt', '.jpg') not in image_files]

    return (len(image_files), len(label_files), len(missing_labels) + len(missing_images))

def main():
    subsets = ['train', 'valid', 'test']
    report_lines = ["📊 DATASET SUMMARY REPORT\n", "=" * 40 + "\n"]

    total_images, total_labels = 0, 0

    for subset in subsets:
        subset_path = os.path.join(dataset_root, subset)
        if os.path.exists(subset_path):
            images, labels, mismatches = count_files(subset_path)
            total_images += images
            total_labels += labels

            report_lines.append(f"\n📁 {subset.upper()} SET:")
            report_lines.append(f"\n - Images: {images}")
            report_lines.append(f"\n - Labels: {labels}")
            report_lines.append(f"\n - Mismatched files: {mismatches}\n")
        else:
            report_lines.append(f"\n⚠️ Folder '{subset}' not found.\n")

    report_lines.append("=" * 40)
    report_lines.append(f"\n✅ TOTAL IMAGES: {total_images}")
    report_lines.append(f"\n✅ TOTAL LABELS: {total_labels}\n")
    report_lines.append("=" * 40 + "\n")

    # Save report
    # with open(summary_file, "w") as f:
    with open(summary_file, "w", encoding="utf-8") as f:
        f.writelines(report_lines)

    print("\n".join(report_lines))
    print(f"\n📄 Summary saved at: {summary_file}")

if __name__ == "__main__":
    main()
