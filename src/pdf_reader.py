import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file or file-like stream.
    """
    if hasattr(pdf_path, "read"):
        # Reset stream pointer if needed
        pdf_path.seek(0)
        document = fitz.open(stream=pdf_path.read(), filetype="pdf")
    else:
        document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text