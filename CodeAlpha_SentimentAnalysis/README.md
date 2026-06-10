# 🎬 Sentiment Analysis — IMDB Movie Reviews
## CodeAlpha Data Analytics Internship — Task 4

## 📌 Project Overview
This project performs Sentiment Analysis on 1000 IMDB movie reviews using
two NLP tools — VADER and TextBlob — to classify reviews as Positive,
Negative, or Neutral and compare their accuracy.

## ❓ Key Questions Explored
1. What is the overall sentiment of IMDB reviews?
2. How accurately can VADER detect sentiment?
3. How accurately can TextBlob detect sentiment?
4. Which model performs better?
5. What words appear most in positive reviews?

## 🔍 Key Findings
- VADER is generally more accurate for short review text
- Most IMDB reviews are strongly positive or negative (few neutral)
- Common positive words: great, love, best, amazing, wonderful
- Common negative words: bad, worst, boring, waste, terrible

## 🛠 Libraries Used
- `pandas` — data loading and manipulation
- `nltk` — VADER sentiment analysis + stopwords
- `textblob` — TextBlob sentiment analysis
- `wordcloud` — word cloud visualization
- `matplotlib` — charts and dashboard
- `seaborn` — styling

## 📁 File Structure
```
CodeAlpha_SentimentAnalysis/
├── main.py                       ← runs everything
├── imdb_reviews.csv              ← raw dataset (auto downloaded)
├── imdb_sentiment_results.csv    ← results with sentiment labels
├── sentiment_dashboard.png       ← 6-chart dashboard
└── README.md
```

## ▶️ How to Run

### Install dependencies
```bash
pip install pandas matplotlib seaborn nltk textblob wordcloud
```

### Run the project
```bash
python main.py
```

## 📷 Dashboard Output
The project generates a 6-chart dashboard:
1. VADER Sentiment Distribution
2. TextBlob Sentiment Distribution
3. Model Accuracy Comparison
4. VADER Score Distribution
5. Actual Sentiment Pie Chart
6. WordCloud of Positive Reviews

---
Made with ❤️ as part of CodeAlpha Data Analytics Internship
