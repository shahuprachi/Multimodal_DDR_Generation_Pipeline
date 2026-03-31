def detect_conflicts(inspection,thermal):
    conflicts =[]
    if "no dampness" in inspection.lower():
        if len(thermal)>0:
            conflicts.append("Inspection report shows no dampness but thermal variation detected.")
    return conflicts