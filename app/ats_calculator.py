def calculate_ats(resume_text, skills):

    score = 0

    # Resume length
    words = len(resume_text.split())

    if words >= 400:
        score += 20
    elif words >= 250:
        score += 15
    else:
        score += 10

    # Skills
    score += min(len(skills) * 4, 30)

    # Sections
    sections = [
        "education",
        "experience",
        "skills",
        "project",
        "certification"
    ]

    for section in sections:
        if section.lower() in resume_text.lower():
            score += 5

    return min(score, 100)