from flask import Flask, render_template, request
from utils.pdf_loader import load_pdf_text
from utils.image_extractor import extract_images

from pipeline.inspection_parser import parse_inspection
from pipeline.thermal_parser import parse_thermal
from pipeline.observation_merger import merge_observations
from pipeline.conflict_engine import detect_conflicts
from pipeline.missing_info_engine import find_missing
from pipeline.severity_engine import calculate_severity
from pipeline.image_mapper import map_images
from pipeline.ddr_writer import generate_ddr

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
IMAGE_FOLDER = "static/extracted_images"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    report = None
    images = []

    if request.method == "POST":

        inspection = request.files["inspection"]
        thermal = request.files["thermal"]

        inspection_path = os.path.join(
            UPLOAD_FOLDER,
            inspection.filename
        )

        thermal_path = os.path.join(
            UPLOAD_FOLDER,
            thermal.filename
        )

        inspection.save(inspection_path)
        thermal.save(thermal_path)

        # Load text
        inspection_text = load_pdf_text(inspection_path)
        thermal_text = load_pdf_text(thermal_path)

        # NLP pipeline
        observations = parse_inspection(inspection_text)
        temperatures = parse_thermal(thermal_text)

        merged = merge_observations(observations)

        conflicts = detect_conflicts(
            inspection_text,
            thermal_text
        )

        missing = find_missing(inspection_text)

        severity = calculate_severity(
            merged,
            temperatures
        )

        # Extract images from inspection PDF
        images = extract_images(inspection_path)

        image_list=images

        # Generate DDR PDF WITH images
        report = generate_ddr(
            inspection_text,
            merged,
            temperatures,
            conflicts,
            missing,
            severity,
            image_list
        )

    return render_template(
        "index.html",
        report=report,
        images=images
    )


if __name__ == "__main__":
    app.run(debug=True)