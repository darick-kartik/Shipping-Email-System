from app.extractors.tonnage_extractor import extract_tonnage
from app.services.preprocessing import clean_text

sample = """
MV BLUE STAR (38K DWT) OPEN 25 MAY GABES
GEARED SELF-TRIMMING SINGLE DECK BULK CARRIER
"""

print(extract_tonnage(sample))



