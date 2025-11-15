# import requests
# import json
# import os

# # TODO: fill these from your Azure Document Intelligence resource
# DOCUMENT_INTELLIGENCE_ENDPOINT = "<YOUR_DOC_INTELLIGENCE_ENDPOINT>"  # e.g. https://aadhaar-ocr-service.cognitiveservices.azure.com
# DOCUMENT_INTELLIGENCE_KEY = "<YOUR_DOC_INTELLIGENCE_KEY>"

# # API version and model
# API_VERSION = "2023-07-31"
# MODEL_ID = "prebuilt-read"

# def extract_text(image_path: str) -> str:
#     """
#     Calls Azure Document Intelligence prebuilt Read model
#     and returns the full OCR text.
#     Also saves the raw OCR text into:
#       ../sample_output/raw_ocr_output.txt
#     """
#     if not os.path.isfile(image_path):
#         raise FileNotFoundError(f"Image not found: {image_path}")

#     url = f"{DOCUMENT_INTELLIGENCE_ENDPOINT}/formrecognizer/documentModels/{MODEL_ID}:analyze?api-version={API_VERSION}"

#     headers = {
#         "Ocp-Apim-Subscription-Key": DOCUMENT_INTELLIGENCE_KEY,
#         "Content-Type": "application/octet-stream",
#     }

#     with open(image_path, "rb") as f:
#         data = f.read()

#     response = requests.post(url, headers=headers, data=data)
#     response.raise_for_status()
#     result = response.json()

#     # For v4.0 APIs, full plain text is in analyzeResult.content
#     all_text = result["analyzeResult"]["content"]

#     # Ensure sample_output folder exists (relative to this file)
#     base_dir = os.path.dirname(os.path.dirname(__file__))  # go up from code/ to ocr_module/
#     sample_output_dir = os.path.join(base_dir, "sample_output")
#     os.makedirs(sample_output_dir, exist_ok=True)

#     raw_output_path = os.path.join(sample_output_dir, "raw_ocr_output.txt")
#     with open(raw_output_path, "w", encoding="utf-8") as f:
#         f.write(all_text)

#     print(f"✅ OCR text saved to {raw_output_path}")
#     return all_text


# if __name__ == "__main__":
#     # Example usage: python ocr_extraction.py data/cleaned/sample_aadhaar.jpg
#     import sys

#     if len(sys.argv) < 2:
#         print("Usage: python ocr_extraction.py <image_path>")
#         sys.exit(1)

#     img_path = sys.argv[1]
#     text = extract_text(img_path)
#     print("\n----- OCR TEXT START -----\n")
#     print(text)
#     print("\n----- OCR TEXT END -----\n")




import re

def clean_ocr_output(text):
    result = {}

    # Extract Aadhaar number (4-4-4 digits)
    aadhaar = re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", text)
    if aadhaar:
        result["aadhaar_number"] = aadhaar.group()

    # Extract English name
    name = re.search(r"[A-Z][A-Za-z ]+ PUSHKARNA", text)
    if name:
        result["name"] = name.group().strip()

    # Extract YOB
    yob = re.search(r"YOB[: ]+(\d{4})", text)
    if yob:
        result["year_of_birth"] = yob.group(1)

    # Extract gender
    gender = re.search(r"\bFemale\b|\bMale\b", text, re.IGNORECASE)
    if gender:
        result["gender"] = gender.group().capitalize()

    return result


sample_text = open("aadhaar_raw_output.txt", "r", encoding="utf-8").read()
print(clean_ocr_output(sample_text))
