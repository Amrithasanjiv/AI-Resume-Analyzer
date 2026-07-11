def extract_skills(text):
    skills = [
        "python",
        "java",
        "c++",
        "sql",
        "mysql",
        "mongodb",
        "html",
        "css",
        "javascript",
        "django",
        "flask",
        "react",
        "nodejs",
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "pandas",
        "numpy",
        "power bi",
        "excel",
        "docker",
        "aws",
        "git",
        "linux",
        # Engineering Skills
        "autocad",
        "solidworks",
        "matlab",
        "plc",
        # HR Skills
        "recruitment",
        "payroll",
        "communication",
        # Accountant Skills
        "tally",
        "gst",
        "taxation",
        # Other Domain Skills
        "marketing",
        "seo",
        "sales",
        "finance",
        "banking",
        "legal",
        "healthcare",
        "medicine",
        "cooking",
        "teaching"
    ]

    text = text.lower()
    found = []

    for skill in skills:
        if skill in text:
            # Handle special acronym formatting where appropriate
            if skill in ["sql", "html", "css", "aws", "plc", "gst", "seo"]:
                found.append(skill.upper())
            elif skill == "c++":
                found.append("C++")
            elif skill == "power bi":
                found.append("Power BI")
            elif skill == "nodejs":
                found.append("Node.js")
            else:
                found.append(skill.title())

    return sorted(list(set(found)))