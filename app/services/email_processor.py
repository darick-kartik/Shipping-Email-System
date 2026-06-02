from app.services.preprocessing import clean_text

from app.classifier.predict import (
    predict_email_category
)

from app.extractors.tonnage_extractor import (
    extract_tonnage
)

from app.extractors.vc_extractor import (
    extract_vc
)

from app.extractors.tc_extractor import (
    extract_tc
)


def process_email(email_text):

    cleaned_text = clean_text(
        email_text
    )

    category = predict_email_category(
        cleaned_text
    )

    if category == "tonnage":

        extracted_data = extract_tonnage(
            cleaned_text
        )

    elif category == "vc":

        extracted_data = extract_vc(
            cleaned_text
        )

    elif category == "tc":

        extracted_data = extract_tc(
            cleaned_text
        )

    else:

        extracted_data = {}

    return {

        "category": category,

        "data": extracted_data
    }