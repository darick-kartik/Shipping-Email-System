from app.database.mongo_connection import (
    emails_collection
)


def save_email(document):

    result = emails_collection.insert_one(
        document
    )

    return str(
        result.inserted_id
    )


def get_all_emails():

    emails = list(
        emails_collection.find()
    )

    for email in emails:

        email["_id"] = str(
            email["_id"]
        )

    return emails


def get_email_by_id(email_id):

    from bson import ObjectId

    email = emails_collection.find_one(
        {
            "_id": ObjectId(email_id)
        }
    )

    if email:

        email["_id"] = str(
            email["_id"]
        )

    return email