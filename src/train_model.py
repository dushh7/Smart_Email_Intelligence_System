import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from preprocess import clean_text


# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv(
    "data/spam.csv",
    header=None,
    names=["raw"]
)

df[["label", "message"]] = df["raw"].str.split(
    "\t",
    n=1,
    expand=True
)

df = df[["label", "message"]]

# -------------------------
# Clean Text
# -------------------------

df["clean_message"] = df["message"].apply(clean_text)

# -------------------------
# TF-IDF
# -------------------------

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["clean_message"])

y = df["label"]

# -------------------------
# Split Data
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------
# Train Model
# -------------------------

model = MultinomialNB()

model.fit(X_train, y_train)

# -------------------------
# Evaluate
# -------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.4f}")

# -------------------------
# Save
# -------------------------

joblib.dump(
    model,
    "models/spam_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/tfidf.pkl"
)

print("Model Saved Successfully")