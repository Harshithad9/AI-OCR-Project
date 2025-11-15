# AI-OCR: Aadhaar Card Data Extraction – Milestone 1 & 2

## 📘 Project Overview
This repository documents the first two milestones of an AI-OCR pipeline designed to extract structured information from Aadhaar card images.

The system extracts:
- Name  
- Date of Birth / Year of Birth  
- Gender  
- Aadhaar Number  

The goal is to build a preprocessing → OCR → validation workflow that will later support fraud detection and custom model training.

> ✅ **Milestone 1: Data Collection & Preprocessing – Completed**  
> ✅ **Milestone 2: OCR Extraction & Validation – Completed**  
> 🔄 **Milestone 3: Fraud Detection (Upcoming)**  

---

# 🎯 Milestone 1 — Data Collection & Preprocessing

### Objectives
- Collect Aadhaar-like synthetic dataset  
- Clean & standardize images  
- Perform data augmentation  
- Prepare annotations  
- Format labels for training  
- Validate dataset integrity  

### Workflow Summary
#### 1) Data Collection  
Dataset used:  
**Roboflow – Aadhar Card Entity Detection (CC BY 4.0)**  
https://universe.roboflow.com/jizo/aadhar-card-entity-detection  

> ⚠️ No real Aadhaar data was used. Only synthetic samples.

#### 2) Image Cleaning
- Removed duplicates  
- Standardized resolution  
- Repaired/corrected corrupted files  

#### 3) Data Augmentation  
- Rotation  
- Noise addition  
- Brightness/Contrast variation  

#### 4) Label Formatting  
- Converted dataset labels into YOLO format  
- Stored bounding boxes & entity metadata  

---

# 🎯 Milestone 2 — OCR Extraction & Field Validation (Completed)

### Objectives
- Use Azure Document Intelligence (Prebuilt Model)  
- Extract Aadhaar text fields  
- Perform rule-based validation  
- Clean & structure the OCR output  
- Prepare JSON outputs  

### Technologies Used
- Azure Document Intelligence (Prebuilt Identity / Read Model)  
- Python (Regex parsing + validation)  
- Azure OpenAI (Optional refinement)  

---

## 🧾 OCR Workflow (Milestone 2)

### 1️⃣ Upload Aadhaar Image to Azure OCR
A synthetic Aadhaar sample was uploaded to the **Prebuilt Identity Model** in Document Intelligence Studio.

### 2️⃣ Extract Text
Azure returned structured paragraphs such as:

भारत सरकार GOVERNMENT OF INDIA
निरुपमा पुष्करणा NIRUPMA PUSHKARNA जन्म वर्ष YOB: 1951 महिला Female
8716 0813 8875
आधार - आम आदमी का अधिकार


Stored in:

### 3️⃣ Field Extraction (Python)
Regex-based Python logic extracts:

- Name: `"NIRUPMA PUSHKARNA"`  
- YOB: `"1951"`  
- Gender: `"Female"`  
- Aadhaar Number: `"8716 0813 8875"`

Saved to:
ocr_module/results/extracted_fields.json

### 4️⃣ Data Validation
Validation checks:
- Aadhaar format: `XXXX XXXX XXXX`  
- Gender: Male / Female  
- YOB: 4-digit year  
- Name: Must be a valid text string  

### 5️⃣ (Optional) Azure OpenAI Refinement
Final cleaned JSON stored in:
ocr_module/results/refined_output.json



---

## 📌 Milestones Progress

| Milestone | Description | Status |
|-----------|-------------|--------|
| 1 | Data Collection & Preprocessing | ✅ Completed |
| 2 | OCR Extraction & Validation | ✅ Completed |
| 3 | Fraud Detection (DL/CV) | 🔄 Upcoming |

---

## 🚀 Next Steps
For Milestone 3:
- Use Deep Learning (YOLO/ResNet) to detect tampering  
- Identify forged Aadhaar elements  
- Highlight mismatches (photo swap, edited text, etc.)  

---

## 📄 License
Licensed under the **MIT License**.  
See the `LICENSE` file for more details.

---

## 🙌 Acknowledgment
Dataset Source:  
Roboflow — *Aadhar Card Entity Detection* (CC BY 4.0)

---

# 🎉 End of README
