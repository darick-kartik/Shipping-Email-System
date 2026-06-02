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

from app.database.email_repository import (
    save_email
)


def process_email(email_text):

    # Step 1: Clean email
    cleaned_text = clean_text(
        email_text
    )

    # Step 2: Predict category
    category = predict_email_category(
        cleaned_text
    )

    # Step 3: Extract data
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

    # Step 4: Create MongoDB document
    document = {

        "raw_email": email_text,

        "category": category,

        "data": extracted_data
    }

    # Step 5: Save to MongoDB
    email_id = save_email(
        document
    )

    # Step 6: Return response
    return {

        "id": email_id,

        "category": category,

        "data": extracted_data
    }