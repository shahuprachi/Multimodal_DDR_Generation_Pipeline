def calculate_severity(observations, temperatures):
    if len(observations) > 5:
        return "High severity due to multiple structural indicators"
    if len(observations) > 2:
        return "Moderate severity based on repeated dampness indicators"
    return "Low severity"