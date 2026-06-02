import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv("training_data/training_data.csv")

# Features and labels
X = df["email_text"]
y = df["category"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("svm", SVC(kernel="linear"))
])

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation
print(classification_report(y_test, predictions))

# Save model
import os
import joblib

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/email_classifier.pkl"
)