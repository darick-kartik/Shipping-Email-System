import re


def clean_text(text):
    """
    Basic email text cleaning
    """

    # Convert to uppercase
    text = text.upper()

    # Replace multiple spaces/newlines with single space
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text