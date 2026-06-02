from app.database.mongo_connection import (
    emails_collection
)


def save_email(document):

    result = emails_collection.insert_one(
        document
    )

    return str(result.inserted_id)