import re


def extract_vessel_name(text):

    vessel_match = re.search(
        r"MV\s+([A-Z0-9\s]+?)(?:\(|DWT|OPEN)",
        text,
        re.IGNORECASE
    )

    if vessel_match:

        vessel_name = vessel_match.group(1).strip()

        vessel_name = re.sub(
            r"\s+\d+K$",
            "",
            vessel_name
        )

        vessel_types = [
            "HANDYSIZE",
            "SUPRAMAX",
            "ULTRAMAX",
            "PANAMAX",
            "KAMSARMAX",
            "CAPESIZE",
            "MR",
            "LR1",
            "LR2",
            "VLCC",
            "AFRAMAX",
            "SUEZMAX"
        ]

        for vessel_type in vessel_types:

            vessel_name = re.sub(
                rf"\b{vessel_type}\b",
                "",
                vessel_name,
                flags=re.IGNORECASE
            )

        vessel_name = " ".join(
            vessel_name.split()
        )

        return vessel_name

    return None


def extract_vessel_size(text):

    size_match = re.search(
        r"DWT\s+(\d+)",
        text,
        re.IGNORECASE
    )

    if not size_match:

        size_match = re.search(
            r"(\d+K)\s*DWT",
            text,
            re.IGNORECASE
        )

    if size_match:
        return size_match.group(1)

    return None


def extract_open_date(text):

    patterns = [

        r"O/A\s+(\d+(?:ST|ND|RD|TH)?\s+[A-Z]+)",

        r"OPEN\s+(\d+\s+[A-Z]+)",

        r"([0-9]{2}-[0-9]{2}\s+[A-Z]+)",

        r"(\d{1,2}\s+[A-Z]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return None


def extract_open_port(text):

    patterns = [

        r"OPEN\s+([A-Z\s]+?),",

        r"OPEN\s+\d+\s+[A-Z]+\s+([A-Z\s]+)",

        r"OPEN\s+([A-Z\s]+)\s+O/A",

        r"OPEN\s+([A-Z\s]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    return None


def extract_vessel_type(text):

    vessel_types = [

        "HANDYSIZE",
        "SUPRAMAX",
        "ULTRAMAX",
        "PANAMAX",
        "KAMSARMAX",
        "CAPESIZE",
        "MR",
        "LR1",
        "LR2",
        "VLCC",
        "AFRAMAX",
        "SUEZMAX",
        "BULK CARRIER"
    ]

    text_upper = text.upper()

    for vessel_type in vessel_types:

        if vessel_type in text_upper:
            return vessel_type

    return None

def extract_account_name(text):

    match = re.search(
        r"ACCOUNT\s*:\s*([A-Z& ]+?)(?=\s+MV|\s+M/V|$)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None

def extract_tonnage(text):

    return {

        "vessel_name":
            extract_vessel_name(text),

        "vessel_size":
            extract_vessel_size(text),

        "open_date":
            extract_open_date(text),

        "open_port":
            extract_open_port(text),

        "vessel_type":
            extract_vessel_type(text),

        "account_name":
            extract_account_name(text)
    }


if __name__ == "__main__":

    sample_text = """
    ACCOUNT: CARGILL

    MV SEA STAR SUPRAMAX 58K DWT
    OPEN SINGAPORE
    15 JULY
    """

    result = extract_tonnage(sample_text)

    print(result)