def parse_inspection(text):
    observations =[]
    keywords=["dampness","seepage","crack","leakage","title gap"]
    lines =text.split("\n")
    for line in lines:
        for keyword in keywords:
            if keyword in line.lower():
                observations.append(line.strip())
    return observations
