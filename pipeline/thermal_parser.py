import re
def parse_thermal(text):
    temps=re.findall(r'\d+\.?\d*\s?°?C', text)
    return temps