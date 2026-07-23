import fitz

def extract_text(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)

    # Store all extracted text
    text = ""

    # Read every page
    for page in doc:
        text += page.get_text()

    # Close the PDF
    doc.close()

    # Return extracted text
    return text 