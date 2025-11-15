import os
import json
import openai

# TODO: fill in your Azure OpenAI values
openai.api_type = "azure"
openai.api_base = "<YOUR_AZURE_OPENAI_ENDPOINT>"   # e.g. https://my-openai-resource.openai.azure.com/
openai.api_key = "<YOUR_AZURE_OPENAI_KEY>"
openai.api_version = "2024-05-01-preview"

AZURE_OPENAI_DEPLOYMENT = "<YOUR_GPT_DEPLOYMENT_NAME>"  # e.g. gpt-4o-mini


def refine_with_openai(ocr_text: str) -> str:
    """
    Sends the OCR text to Azure OpenAI and asks it to:
    - clean noise
    - extract Name, DOB, Gender, Aadhaar Number
    - return JSON string
    """
    prompt = f"""
    You are a helpful assistant. From the following OCR text of an Aadhaar card,
    extract and correct these fields:
    - Name
    - DOB (in DD/MM/YYYY format)
    - Gender
    - Aadhaar Number (XXXX XXXX XXXX)

    Return ONLY valid JSON like:
    {{
      "Name": "...",
      "DOB": "...",
      "Gender": "...",
      "Aadhaar Number": "..."
    }}

    OCR text:
    {ocr_text}
    """

    response = openai.ChatCompletion.create(
        engine=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response["choices"][0]["message"]["content"]
    return content


if __name__ == "__main__":
    # Load OCR text
    base_dir = os.path.dirname(os.path.dirname(__file__))  # ocr_module/
    sample_output_dir = os.path.join(base_dir, "sample_output")
    raw_output_path = os.path.join(sample_output_dir, "raw_ocr_output.txt")

    if not os.path.isfile(raw_output_path):
        print(f"❌ OCR output not found at {raw_output_path}. Run ocr_extraction.py first.")
        exit(1)

    with open(raw_output_path, "r", encoding="utf-8") as f:
        text = f.read()

    refined_json_str = refine_with_openai(text)

    # Save response as refined_output.json
    refined_path = os.path.join(sample_output_dir, "refined_output.json")
    with open(refined_path, "w", encoding="utf-8") as f:
        f.write(refined_json_str)

    print(f"✅ Refined output saved to {refined_path}")
    print("\nModel response:\n", refined_json_str)
