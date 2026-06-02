from app.classifier.predict import (
    predict_email_category
)

samples = [

    "MV PACIFIC STAR 58K DWT OPEN DALIAN",

    "LOAD PORT KANDLA DISCHARGE PORT DUBAI CARGO CLINKER",

    "DELIVERY VANCOUVER REDELIVERY CHITTAGONG 1 TCT"
]


for sample in samples:

    print(
        sample
    )

    print(
        predict_email_category(
            sample
        )
    )

    print("-" * 50)