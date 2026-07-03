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
        "linux"

    ]

    text = text.lower()

    found = []

    for skill in skills:

        if skill in text:

            found.append(skill.title())

    return sorted(found)