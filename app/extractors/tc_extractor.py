import re


def extract_delivery_port(text):

    match = re.search(
        r"DELIVERY[:\s]+(.*?)\s+REDELIVERY",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_redelivery_port(text):

    match = re.search(
        r"REDELIVERY[:\s]+(.*?)(?:\s+DURATION|\s+CARGO|\s+LAYCAN|$)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_duration(text):

    match = re.search(
        r"DURATION[:\s]+(.*?)(?:\s+CARGO|\s+LAYCAN|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    match = re.search(
        r"(\d+\s*TCT)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None

def extract_cargo_name(text):

    match = re.search(
        r"CARGO[:\s]+(.*?)(?:\s+LAYCAN|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return None


def extract_laycan(text):

    match = re.search(
        r"LAYCAN[:\s]+([A-Z0-9\s\-]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_cargo_type(text):

    cargo_types = [

        "COAL",
        "UREA",
        "WHEAT",
        "BARLEY",
        "CLINKER",
        "CEMENT",
        "FERTILIZER",
        "IRON ORE",
        "STEEL COILS",
        "SCRAP",
        "GYPSUM",
        "PETCOKE",
        "HRC"
    ]

    text_upper = text.upper()

    for cargo in cargo_types:

        if cargo in text_upper:
            return cargo

    return None


def extract_account_name(text):

    match = re.search(
        r"ACCOUNT\s*:\s*([A-Z& ]+?)(?=\s+DELIVERY|\s+REDELIVERY|\s+DURATION|\s+CARGO|\s+LAYCAN|$)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_tc(text):

    return {

        "account_name":
            extract_account_name(text),

        "delivery_port":
            extract_delivery_port(text),

        "redelivery_port":
            extract_redelivery_port(text),

        "duration":
            extract_duration(text),

        "cargo_name":
            extract_cargo_name(text),

        "laycan":
            extract_laycan(text),

        "cargo_type":
            extract_cargo_type(text)
    }


if __name__ == "__main__":

    sample_text = """
    ACCOUNT: CARGILL

    DELIVERY VANCOUVER
    REDELIVERY JAPAN

    DURATION 6-8 MONTHS

    CARGO COAL

    LAYCAN MID JULY
    """

    print(extract_tc(sample_text))