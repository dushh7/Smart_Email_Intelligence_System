import streamlit as st
import sys
import os

# Add src folder to path
sys.path.append(os.path.abspath("src"))

from predict import predict_email
from sentiment import analyze_sentiment
from keywords import extract_keywords
from summarizer import summarize_text
from ner import extract_entities


# ------------------------------------
# Page Configuration
# ------------------------------------

st.set_page_config(
    page_title="Smart Email Intelligence System",
    page_icon="📧",
    layout="wide"
)

# ------------------------------------
# Title
# ------------------------------------

st.title("📧 Smart Email Intelligence System")
st.markdown(
    """
    NLP-Based Email Analysis Dashboard

    Features:
    - Spam Detection
    - Sentiment Analysis
    - Keyword Extraction
    - Named Entity Recognition
    - Text Summarization
    """
)

st.divider()

# ------------------------------------
# Email Input
# ------------------------------------

email_text = st.text_area(
    "Paste Email / Message Here",
    height=250
)

# ------------------------------------
# Analyze Button
# ------------------------------------

if st.button("Analyze Email"):

    if not email_text.strip():
        st.warning("Please enter an email/message.")
        st.stop()

    # --------------------------------
    # Spam Detection
    # --------------------------------

    spam_result = predict_email(email_text)

    # --------------------------------
    # Sentiment
    # --------------------------------

    sentiment_result = analyze_sentiment(email_text)

    # --------------------------------
    # Keywords
    # --------------------------------

    keywords_result = extract_keywords(email_text)

    # --------------------------------
    # Summary
    # --------------------------------

    summary_result = summarize_text(email_text)

    # --------------------------------
    # NER
    # --------------------------------

    entities_result = extract_entities(email_text)

    st.divider()

    # ==================================
    # RESULTS
    # ==================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📨 Spam Detection")

        if spam_result.lower() == "spam":
            st.error("SPAM")
        else:
            st.success("HAM")

    with col2:

        st.subheader("😊 Sentiment")

        if sentiment_result == "Positive":
            st.success(sentiment_result)

        elif sentiment_result == "Negative":
            st.error(sentiment_result)

        else:
            st.info(sentiment_result)

    st.divider()

    # ==================================
    # KEYWORDS
    # ==================================

    st.subheader("🔑 Keywords")

    if keywords_result:

        for keyword in keywords_result:
            st.write("•", keyword)

    else:
        st.write("No keywords found.")

    st.divider()

    # ==================================
    # ENTITIES
    # ==================================

    st.subheader("🏷 Named Entities")

    if entities_result:

        for entity in entities_result:

            st.write(
                f"{entity['text']}  →  {entity['label']}"
            )

    else:

        st.write("No entities detected.")

    st.divider()

    # ==================================
    # SUMMARY
    # ==================================

    st.subheader("📝 Summary")

    st.write(summary_result)

    st.divider()

    st.success("Analysis Completed Successfully")