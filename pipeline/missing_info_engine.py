def find_missing(text):
    required_sections = [
        "roof",
        "bathroom",
        "kitchen"
    ]
    missing = []
    for section in required_sections:
        if section not in text.lower():
            missing.append(f"{section} inspection: Not Available")
    return missing