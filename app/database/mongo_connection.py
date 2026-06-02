from pymongo import MongoClient


client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["shipping_email_db"]

emails_collection = db["emails"]