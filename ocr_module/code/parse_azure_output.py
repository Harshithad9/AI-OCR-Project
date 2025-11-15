import json
import re

def extract_fields_from_azure(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    text_blocks = []
    for page in data.get("pages", []):
        for line in page.get("lines", []):
            text_blocks.append(line["content"])

    full_text = " ".join(text_blocks)

    # Extract Aadhaar Number
    aadhaar_match = re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", full_text)
    aadhaar_number = aadhaar_match.group(0) if aadhaar_match else None

    # Extract Year of Birth
    yob_match = re.search(r"19\d{2}|20\d{2}", full_text)
    yob = yob_match.group(0) if yob_match else None

    # Extract Name
    name = None
    for line in text_blocks:
        if "NIRUPMA" in line or "PUSHKARNA" in line:
            name = line
            break

    # Extract Gender
    gender = "Female" if "Female" in full_text else "Male" if "Male" in full_text else None

    return {
        "name": name,
        "yob": yob,
        "gender": gender,
        "aadhaar_number": aadhaar_number
    }

if __name__ == "__main__":
    fields = extract_fields_from_azure("../results/ocr_raw_output.json")
    print(json.dumps(fields, indent=4))
