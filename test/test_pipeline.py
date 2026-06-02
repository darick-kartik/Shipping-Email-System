from app.services.email_processor import process_email


sample = """
LOAD PORT THAILAND
DISCHARGE PORT KANDLA
LAYCAN MID JULY
"""

result = process_email(sample)

print(result)