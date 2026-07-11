from job_profiles import JOB_SKILLS


def get_missing_skills(category, found):
    required = JOB_SKILLS.get(category, [])
    found_lower = [s.lower() for s in found]
    missing = []

    for skill in required:
        if skill.lower() not in found_lower:
            missing.append(skill)

    return missing