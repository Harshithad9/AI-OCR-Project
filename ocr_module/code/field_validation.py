import re
import json
import os


def extract_fields(text: str) -> dict:
    """
    Extracts key Aadhaar fields from OCR text using regex.
    - Name
    - DOB
    - Gender
    - Aadhaar Number
    """
    fields = {}

    # Name: look for "Name" and capture following words
    name = re.search(r"Name[:\s]*([A-Za-z ]{3,})", text)
    fields["Name"] = name.group(1).strip() if name else None

    # DOB: DD/MM/YYYY or DD-MM-YYYY
    dob = re.search(r"(\d{2}[/-]\d{2}[/-]\d{4})", text)
    fields["DOB"] = dob.group(1) if dob else None

    # Gender: Male/Female (case-insensitive)
    gender = re.search(r"\b(Male|MALE|Female|FEMALE)\b", text)
    fields["Gender"] = gender.group(1).capitalize() if gender else None

    # Aadhaar Number: 4-4-4 digits with space
    aadhaar = re.search(r"(\d{4}\s\d{4}\s\d{4})", text)
    fields["Aadhaar Number"] = aadhaar.group(1) if aadhaar else None

    return fields


def validate_fields(fields: dict) -> list:
    """
    Validate extracted fields against simple format rules.
    Returns a list of error messages (empty list = all good).
    """
    errors = []

    # Name must exist and be at least 3 chars
    if not fields.get("Name") or len(fields["Name"]) < 3:
        errors.append("Invalid or missing Name")

    # DOB must exist
    if not fields.get("DOB"):
        errors.append("Invalid or missing DOB")

    # Gender must be Male/Female
    if fields.get("Gender") not in ["Male", "Female"]:
        errors.append("Invalid or missing Gender")

    # Aadhaar number check
    aadhaar = fields.get("Aadhaar Number")
    if not aadhaar or not re.fullmatch(r"\d{4}\s\d{4}\s\d{4}", aadhaar):
        errors.append("Invalid or missing Aadhaar Number")

    return errors


if __name__ == "__main__":
    # Load the OCR text from sample_output/raw_ocr_output.txt
    base_dir = os.path.dirname(os.path.dirname(__file__))  # ocr_module/
    sample_output_dir = os.path.join(base_dir, "sample_output")
    raw_output_path = os.path.join(sample_output_dir, "raw_ocr_output.txt")

    if not os.path.isfile(raw_output_path):
        print(f"❌ OCR output not found at {raw_output_path}. Run ocr_extraction.py first.")
        exit(1)

    with open(raw_output_path, "r", encoding="utf-8") as f:
        text = f.read()

    fields = extract_fields(text)
    errors = validate_fields(fields)

    # Save extracted fields
    extracted_path = os.path.join(sample_output_dir, "extracted_fields.json")
    with open(extracted_path, "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=4, ensure_ascii=False)

    print(f"✅ Extracted fields saved to {extracted_path}")
    print("Extracted fields:", json.dumps(fields, indent=4))

    if errors:
        print("\n❌ Validation errors:")
        for e in errors:
            print(" -", e)
    else:
        print("\n✅ All fields passed validation.")
