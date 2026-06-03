import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):

    score = sia.polarity_scores(text)

    if score["compound"] >= 0.05:
        return "Positive"

    elif score["compound"] <= -0.05:
        return "Negative"

    else:
        return "Neutral"


if __name__ == "__main__":

    sample = input("Enter text: ")

    print(analyze_sentiment(sample))