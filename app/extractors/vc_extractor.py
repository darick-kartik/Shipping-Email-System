import re


def extract_loading_port(text):

    match = re.search(
        r"LOAD PORT[:\s]+(.*?)\s+DISCHARGE PORT",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_discharge_port(text):

    match = re.search(
        r"DISCHARGE PORT[:\s]+(.*?)(?:\s+LAYCAN|\s+CARGO|$)",
        text,
        re.IGNORECASE
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


def extract_cargo_name(text):

    match = re.search(
        r"CARGO[:\s]+(.*?)(?:\s+LAYCAN|$)",
        text,
        re.IGNORECASE | re.DOTALL
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
        r"ACCOUNT\s*:\s*([A-Z& ]+?)(?=\s+LOAD PORT|\s+DISCHARGE PORT|\s+CARGO|\s+LAYCAN|$)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_vc(text):

    return {

        "account_name":
            extract_account_name(text),

        "cargo_name":
            extract_cargo_name(text),

        "loading_port":
            extract_loading_port(text),

        "discharge_port":
            extract_discharge_port(text),

        "laycan":
            extract_laycan(text),

        "cargo_type":
            extract_cargo_type(text)
    }


if __name__ == "__main__":

    sample_text = """
    ACCOUNT: CARGILL

    LOAD PORT KOH SI CHANG THAILAND
    DISCHARGE PORT KANDLA

    CARGO CLINKER

    LAYCAN MID JULY
    """

    print(extract_vc(sample_text))