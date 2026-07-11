def generate_suggestions(score, missing_skills):

    suggestions = []

    if score < 70:
        suggestions.append(
            "Increase resume length by adding more projects."
        )

    if len(missing_skills):

        suggestions.append(
            "Add missing technical skills if you have experience with them."
        )

    suggestions.append(
        "Include measurable achievements."
    )

    suggestions.append(
        "Add GitHub profile."
    )

    suggestions.append(
        "Include certifications."
    )

    return suggestions