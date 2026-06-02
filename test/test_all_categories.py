from app.services.email_processor import process_email

emails = [

    """
    ACCOUNT: CARGILL
    MV SEA STAR SUPRAMAX 58K DWT
    OPEN SINGAPORE
    15 JULY
    """,

    """
    ACCOUNT: BUNGE
    LOAD PORT KANDLA
    DISCHARGE PORT DUBAI
    CARGO CLINKER
    LAYCAN MID JULY
    """,

    """
    ACCOUNT: ADM
    DELIVERY VANCOUVER
    REDELIVERY JAPAN
    DURATION 6-8 MONTHS
    CARGO COAL
    LAYCAN MID JULY
    """
]

for email in emails:

    result = process_email(email)

    print("\n" + "=" * 50)
    print(result)