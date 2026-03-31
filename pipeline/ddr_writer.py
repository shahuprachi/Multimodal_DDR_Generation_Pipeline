from fpdf import FPDF
import os


def generate_ddr(
        inspection_text,
        observations,
        temperatures,
        conflicts,
        missing,
        severity,
        image_paths=None
):

    print("DDR FUNCTION EXECUTED")  # Debug confirmation

    # ===============================
    # BUILD DDR REPORT CONTENT
    # ===============================

    report = f"""
==============================
DETAILED DEFECT REPORT (DDR)
==============================

1. Property Issue Summary
------------------------
"""

    if observations:
        report += ", ".join(observations) + "\n"
    else:
        report += "No major issues detected.\n"

    report += """

2. Area-wise Observations
------------------------
"""

    if observations:
        for obs in observations:
            report += f"- {obs}\n"
    else:
        report += "No area-wise issues recorded.\n"

    report += f"""

3. Probable Root Cause
---------------------
Possible structural moisture intrusion
Ventilation issues
Material ageing or leakage pathways

4. Severity Assessment
---------------------
Overall Severity Level:
{severity if severity else "Not Available"}

5. Recommended Actions
---------------------
Conduct detailed site verification
Repair affected structural components
Monitor moisture spread using thermal tools
Schedule maintenance follow-up inspection

6. Additional Notes
------------------
Inspection Data Length: {len(inspection_text) if inspection_text else 0} characters
Thermal Observations Count: {len(temperatures) if temperatures else 0}

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

    print("DEBUG REPORT CONTENT:\n", report)  # Debug check

    # ===============================
    # CREATE PDF
    # ===============================

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "", 12)

    # Fix encoding issues (important)
    safe_report = report.encode("latin-1", "replace").decode("latin-1")

    # Write full report at once (fixes blank PDF issue)
    pdf.multi_cell(0, 8, safe_report)

    # ===============================
    # ADD IMAGES TO PDF (MULTIMODAL)
    # ===============================

    if image_paths:

        pdf.add_page()
        pdf.set_font("Helvetica", "", 14)
        pdf.cell(0, 10, "Inspection Images", ln=True)

        for img_path in image_paths:

            if os.path.exists(img_path):

                try:
                    pdf.image(img_path, x=10, w=170)
                    pdf.ln(10)

                except Exception as e:

                    pdf.set_font("Helvetica", "", 10)
                    pdf.cell(0, 10, f"Could not load image: {img_path}", ln=True)

            else:

                pdf.set_font("Helvetica", "", 10)
                pdf.cell(0, 10, f"Image not found: {img_path}", ln=True)

    # ===============================
    # SAVE PDF FILE
    # ===============================

    output_file = "generated_ddr.pdf"

    pdf.output(output_file)

    print(f"DDR PDF successfully generated: {output_file}")

    return report