# AI-OCR: Aadhaar Card Data Extraction – Milestone 1

## 📘 Project Overview
This repository documents **Milestone 1 (Data Collection & Preprocessing)** of an ongoing AI-OCR project focused on extracting structured information from Aadhaar card images, including:

- Name  
- Date of Birth (DOB)  
- Gender  
- Aadhaar Number  
- Address *(future scope)*  

The processed dataset produced here will be used later for **model training, validation, and integration** (Azure AI Document Intelligence + Custom DL models).

> ✅ **Current Status:** Milestone 1 Completed  
> 🔄 **Milestone 2:** In Progress  

---

## 🎯 Milestone 1 Objectives
- Collect Aadhaar-like synthetic document images  
- Clean and standardize image formats  
- Perform data augmentation  
- Annotate fields visually  
- Convert labels into training-compatible format  
- Validate dataset compatibility for OCR  

---

## 🗂️ Workflow Summary (Milestone 1)

### ✅ 1) Data Collection
- Gathered synthetic Aadhaar card samples  
- Source dataset:  
  **Roboflow – Aadhar Card Entity Detection (CC BY 4.0)**  
  https://universe.roboflow.com/jizo/aadhar-card-entity-detection  

> ⚠️ Only synthetic/anonymized images are used.  
> No real Aadhaar data or personal information included.  

---

### ✅ 2) Image Cleaning
Performed:
- Duplicate removal  
- Corrupt file elimination  
- Standardizing resolution  

**Tools:** OpenCV  

---

### ✅ 3) Data Augmentation
Applied transformations to increase image variability:
- Rotation  
- Brightness / Contrast adjustment  
- Noise addition  

**Library:** Albumentations  

---

### ✅ 4) Label Formatting
- Converted annotations into YOLO format  
- Stored metadata & bounding boxes for training  

**Tools:** Python, Pandas  

---

## 📁 Project Structure (current)




