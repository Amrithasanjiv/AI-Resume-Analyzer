# 📄 Resumatic — AI Resume Analyzer & Matcher

Resumatic is a professional, AI-powered Resume Analyzer built to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). Using Machine Learning, Natural Language Processing (NLP), and parsing algorithms, Resumatic evaluates resumes, categorizes them across 24 job domains, extracts key technical skills, and matches them against target job descriptions.

---

## 🚀 Key Features

* **AI Category Classification**: Classifies resumes into one of 24 distinct professional domains (e.g., *Information Technology, Finance, Healthcare, Engineering*) using a trained Machine Learning model.
* **Dynamic ATS Scoring**: Calculates an instant ATS match score out of 100 based on keyword density, section completeness, formatting metrics, and length.
* **Target Job Matching**: Paste a target job description to dynamically run a skill gap analysis, highlighting matching skills and missing credentials.
* **Prioritized Improvement Suggestions**: Generates actionable feedback to optimize resumes for better visibility.
* **Clean Single-Page UI**: A premium dark-theme interface built with Streamlit and styled with CSS.

---

## 🛠️ Tech Stack

* **Frontend & Dashboard**: Streamlit, Custom CSS
* **Natural Language Processing & Parsing**: PyMuPDF (fitz), BeautifulSoup4, NLTK
* **Machine Learning**: Scikit-learn, Joblib, TF-IDF Vectorization, LinearSVC
* **Data Processing**: Pandas, NumPy

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Amrithasanjiv/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Set Up Virtual Environment
Create and activate a python virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all package requirements:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

Start the Streamlit application server:
```bash
streamlit run app/app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser to launch the web dashboard.

---

## 🧠 Model Architecture

The resume classification pipeline uses a **Linear Support Vector Classification (LinearSVC)** model trained on categorized resume text datasets.
1. **Extraction**: Plain text is extracted from PDF uploads.
2. **Preprocessing**: Cleans raw text by removing HTML tags, URLs, special characters, stopwords, and applies NLTK WordNet Lemmatization.
3. **Vectorization**: Transforms cleaned text tokens using a pre-trained **TF-IDF Vectorizer**.
4. **Classification**: Predicts the best-fitting job domain from 24 supported target classes.

---

## 📄 License
This project is licensed under the MIT License.