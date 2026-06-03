import joblib
from preprocess import clean_text

# Load model
model = joblib.load("models/spam_model.pkl")

# Load vectorizer
vectorizer = joblib.load("models/tfidf.pkl")


def predict_email(text):
    """
    Predict whether email/message is spam or ham.
    """

    cleaned_text = clean_text(text)

    vectorized_text = vectorizer.transform([cleaned_text])

    prediction = model.predict(vectorized_text)[0]

    return prediction


if __name__ == "__main__":

    sample_text = input("Enter Message: ")

    result = predict_email(sample_text)

    print(f"\nPrediction: {result}")