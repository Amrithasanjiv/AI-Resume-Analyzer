from predictor import ResumePredictor
from pdf_reader import extract_text_from_pdf

# Load predictor
predictor = ResumePredictor()

# PDF file path
pdf_path = "sample_resume.pdf"

# Extract text
resume_text = extract_text_from_pdf(pdf_path)

print("=" * 60)
print("Extracted Resume")
print("=" * 60)

# Print first 500 characters
print(resume_text[:500])

print("\n")

# Predict category
category = predictor.predict(resume_text)

print("=" * 60)
print("Predicted Category")
print("=" * 60)

print(category)