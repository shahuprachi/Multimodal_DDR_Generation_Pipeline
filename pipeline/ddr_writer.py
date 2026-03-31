def generate_ddr(
        inspection_text,
        observations,
        temperatures,
        conflicts,
        missing,
        severity
):

    report = f"""
==============================
DETAILED DEFECT REPORT (DDR)
==============================


1. Property Issue Summary
------------------------
The inspection identified the following key concerns:

{", ".join(observations) if observations else "No major issues detected."}


2. Area-wise Observations
------------------------
"""

    for obs in observations:
        report += f"- {obs}\n"


    report += f"""


3. Probable Root Cause
---------------------
Based on inspection and available thermal indicators:

Possible structural moisture intrusion
Ventilation issues
Material ageing or leakage pathways


4. Severity Assessment
---------------------
Overall Severity Level:

{severity}


5. Recommended Actions
---------------------
Recommended next steps:

Conduct detailed site verification
Repair affected structural components
Monitor moisture spread using thermal tools
Schedule maintenance follow-up inspection


6. Additional Notes
------------------
Inspection Data Length: {len(inspection_text)} characters
Thermal Observations Count: {len(temperatures)}


7. Missing Information
---------------------
"""

    if missing:
        for item in missing:
            report += f"- {item}\n"
    else:
        report += "No missing inspection information detected.\n"


    report += """


8. Conflict Detection Summary
----------------------------
"""

    if conflicts:
        for conflict in conflicts:
            report += f"- {conflict}\n"
    else:
        report += "No conflicts detected between inspection and thermal data.\n"


    return report