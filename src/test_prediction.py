from predictor import ResumePredictor

predictor = ResumePredictor()

resume = """
PROFESSIONAL SUMMARY

Finance professional with experience in accounting, taxation, budgeting, financial reporting, auditing, payroll processing, and GST filing. Strong knowledge of Tally ERP, Microsoft Excel, financial analysis, and bookkeeping.

SKILLS

Accounting
Financial Reporting
GST
Income Tax
Payroll
Tally ERP
Microsoft Excel
Auditing
Budget Planning

EXPERIENCE

Prepared monthly financial reports and managed company accounts.

Handled tax filing and bank reconciliation.

EDUCATION

Bachelor of Commerce
"""

category = predictor.predict(resume)

print("=" * 50)
print("Predicted Category")
print("=" * 50)
print(category)