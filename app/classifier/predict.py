import joblib

model = joblib.load(
    "models/email_classifier.pkl"
)


def predict_email_category(email_text):

    prediction = model.predict(
        [email_text]
    )[0]

    return prediction


if __name__ == "__main__":

    while True:

        email = input(
            "\nEnter Email Text:\n"
        )

        result = predict_email_category(
            email
        )

        print(
            "\nPredicted Category:",
            result
        )