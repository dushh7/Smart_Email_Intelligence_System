# 📧 Smart Email Intelligence System

## Overview

Smart Email Intelligence System is an NLP-powered application that analyzes email content using Machine Learning and Natural Language Processing techniques.

The system provides spam detection, sentiment analysis, keyword extraction, named entity recognition (NER), and text summarization through an interactive Streamlit dashboard.

---

## Features

### Spam Detection
Classifies emails as Spam or Ham using Machine Learning.

### Sentiment Analysis
Determines whether email content is Positive, Negative, or Neutral.

### Keyword Extraction
Identifies important keywords from email text.

### Named Entity Recognition (NER)
Extracts entities such as:
- Organizations
- Locations
- Dates
- People

### Text Summarization
Generates concise summaries of lengthy emails.

### Interactive Dashboard
Provides a user-friendly interface using Streamlit.

---

## Technologies Used

### Python
Core programming language used for development.

### Scikit-Learn
Used for:
- TF-IDF Vectorization
- Spam Classification

### NLTK
Used for:
- Text Preprocessing
- Stopword Removal
- Sentiment Analysis

### SpaCy
Used for:
- Keyword Extraction
- Named Entity Recognition

### Streamlit
Used for building the interactive web application.

### Joblib
Used for model serialization and loading.

---

## Machine Learning Workflow

1. Data Collection
2. Text Preprocessing
3. Feature Extraction using TF-IDF
4. Model Training using Naive Bayes
5. Model Evaluation
6. Deployment using Streamlit

---

## Project Structure

```text
Smart_Email_Intelligence_System/
│
├── app/
│   └── app.py
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   ├── sentiment.py
│   ├── keywords.py
│   ├── summarizer.py
│   ├── ner.py
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Smart_Email_Intelligence_System.git
```

### Navigate to Project

```bash
cd Smart_Email_Intelligence_System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app/app.py
```

---

## Model Performance

Spam Detection Accuracy:

```text
97.31%
```

---

## Future Enhancements

- Deep Learning Models
- Email Classification Categories
- Multi-Language Support
- Email Priority Prediction
- Advanced Summarization Models

---

## Author

Dushyan S