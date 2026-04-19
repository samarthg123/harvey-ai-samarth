import pdfplumber
import re

# This is a very basic contract extractor. It uses pdfplumber to extract text from a PDF, then uses regex to find parties, obligations, and termination clauses. 
# This is just a starting point and can be improved with more sophisticated NLP techniques like OCR to actually take in contract documents.

def extract_contract_info(pdf_path):
    # 1. text extraction
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    # normalize
    text = text.replace("\n", " ")

    # 2. extract parties (very naive)
    parties = []
    match = re.search(r"between (.+?) and (.+?)[\.,]", text, re.IGNORECASE)
    if match:
        parties = [match.group(1).strip(), match.group(2).strip()]

    # 3. extract obligations KW: shall
    obligations = re.findall(r"([^.]*\bshall\b[^.]*)\.", text, re.IGNORECASE)

    # 4. extract terminator clause
    termination = re.findall(r"([^.]*\bterminate\b[^.]*)\.", text, re.IGNORECASE)

    return {
        "parties": parties,
        "obligations": obligations[:5],   # limit for sanity
        "termination": termination[:5]
    }

# Run
result = extract_contract_info("contract.pdf")
print(result)