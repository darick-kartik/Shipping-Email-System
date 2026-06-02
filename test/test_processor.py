from app.services.email_processor import (
    process_email
)

email = """
ACCOUNT: CARGILL

MV SEA STAR SUPRAMAX 58K DWT
OPEN SINGAPORE
15 JULY
"""

result = process_email(email)

print(result)