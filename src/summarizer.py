import re

def summarize_text(text, max_sentences=2):

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    if len(sentences) <= max_sentences:
        return text

    return " ".join(sentences[:max_sentences])


if __name__ == "__main__":

    text = input("Enter text:\n")

    print("\nSummary:\n")

    print(summarize_text(text))