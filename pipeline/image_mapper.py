def map_images(images):
    mapped = {}
    for img in images:
        if "bathroom" in img.lower():
            mapped.setdefault("Bathroom", []).append(img)
        else:
            mapped.setdefault("General", []).append(img)
    return mapped