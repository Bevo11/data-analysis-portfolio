import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk
import re

# =====================
# STEP 1: DOWNLOAD NLTK DATA
# =====================
print("=" * 40)
print("STEP 1: Downloading NLTK data...")
print("=" * 40)
nltk.download('vader_lexicon', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
print("  NLTK data ready!")

# =====================
# STEP 2: LOAD DATA
# =====================
print("\n" + "=" * 40)
print("STEP 2: Loading IMDB dataset...")
print("=" * 40)

url = "https://raw.githubusercontent.com/Ankit152/IMDB-sentiment-analysis/master/IMDB-Dataset.csv"
df = pd.read_csv(url)
df.to_csv("imdb_reviews.csv", index=False)
print(f"  Dataset loaded! Shape: {df.shape}")
print(df.head())

# Use a sample of 1000 reviews for speed
df = df.sample(1000, random_state=42).reset_index(drop=True)
print(f"  Working with 1000 sample reviews")

# =====================
# STEP 3: CLEAN TEXT
# =====================
print("\n" + "=" * 40)
print("STEP 3: Cleaning text...")
print("=" * 40)

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)        # remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text) # remove special characters
    text = text.lower().strip()              # lowercase
    return text

df["cleaned_review"] = df["review"].apply(clean_text)
print("  Text cleaned!")
print(df[["review", "cleaned_review"]].head(2))

# =====================
# STEP 4: SENTIMENT ANALYSIS
# =====================
print("\n" + "=" * 40)
print("STEP 4: Running Sentiment Analysis...")
print("=" * 40)

# --- VADER ---
sia = SentimentIntensityAnalyzer()

def get_vader_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def get_vader_score(text):
    return sia.polarity_scores(text)["compound"]

df["vader_sentiment"] = df["cleaned_review"].apply(get_vader_sentiment)
df["vader_score"] = df["cleaned_review"].apply(get_vader_score)

# --- TextBlob ---
def get_textblob_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def get_textblob_score(text):
    return TextBlob(text).sentiment.polarity

df["textblob_sentiment"] = df["cleaned_review"].apply(get_textblob_sentiment)
df["textblob_score"] = df["cleaned_review"].apply(get_textblob_score)

df.to_csv("imdb_sentiment_results.csv", index=False)
print("  Sentiment analysis complete!")
print(df[["cleaned_review", "vader_sentiment", "textblob_sentiment"]].head())

# =====================
# STEP 5: ANALYSIS
# =====================
print("\n" + "=" * 40)
print("STEP 5: Key Analysis")
print("=" * 40)

print("\nVADER Sentiment Distribution:")
print(df["vader_sentiment"].value_counts())

print("\nTextBlob Sentiment Distribution:")
print(df["textblob_sentiment"].value_counts())

# Accuracy vs actual labels
df["actual"] = df["sentiment"].str.capitalize()
vader_accuracy = (df["vader_sentiment"] == df["actual"]).mean() * 100
textblob_accuracy = (df["textblob_sentiment"] == df["actual"]).mean() * 100
print(f"\nVADER Accuracy:    {vader_accuracy:.1f}%")
print(f"TextBlob Accuracy: {textblob_accuracy:.1f}%")

# =====================
# STEP 6: VISUALIZATIONS
# =====================
print("\n" + "=" * 40)
print("STEP 6: Creating visualizations...")
print("=" * 40)

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle("IMDB Movie Reviews — Sentiment Analysis", fontsize=18, fontweight="bold")

colors = {"Positive": "mediumseagreen", "Negative": "tomato", "Neutral": "steelblue"}

# Chart 1 — VADER Sentiment Distribution
vader_counts = df["vader_sentiment"].value_counts()
axes[0, 0].bar(vader_counts.index,
               vader_counts.values,
               color=[colors.get(s, "gray") for s in vader_counts.index],
               edgecolor="black")
axes[0, 0].set_title("VADER Sentiment Distribution")
axes[0, 0].set_ylabel("Number of Reviews")
for i, v in enumerate(vader_counts.values):
    axes[0, 0].text(i, v + 5, str(v), ha="center", fontweight="bold")

# Chart 2 — TextBlob Sentiment Distribution
tb_counts = df["textblob_sentiment"].value_counts()
axes[0, 1].bar(tb_counts.index,
               tb_counts.values,
               color=[colors.get(s, "gray") for s in tb_counts.index],
               edgecolor="black")
axes[0, 1].set_title("TextBlob Sentiment Distribution")
axes[0, 1].set_ylabel("Number of Reviews")
for i, v in enumerate(tb_counts.values):
    axes[0, 1].text(i, v + 5, str(v), ha="center", fontweight="bold")

# Chart 3 — Accuracy Comparison
tools = ["VADER", "TextBlob"]
accuracies = [vader_accuracy, textblob_accuracy]
bars = axes[0, 2].bar(tools, accuracies, color=["steelblue", "coral"], edgecolor="black")
axes[0, 2].set_title("Model Accuracy Comparison")
axes[0, 2].set_ylabel("Accuracy (%)")
axes[0, 2].set_ylim(0, 100)
for bar, acc in zip(bars, accuracies):
    axes[0, 2].text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 1,
                    f"{acc:.1f}%", ha="center", fontweight="bold")

# Chart 4 — VADER Score Distribution
axes[1, 0].hist(df["vader_score"], bins=30, color="steelblue", edgecolor="black")
axes[1, 0].axvline(x=0.05, color="green", linestyle="--", label="Positive threshold")
axes[1, 0].axvline(x=-0.05, color="red", linestyle="--", label="Negative threshold")
axes[1, 0].set_title("VADER Score Distribution")
axes[1, 0].set_xlabel("Compound Score")
axes[1, 0].set_ylabel("Count")
axes[1, 0].legend()

# Chart 5 — Actual Sentiment Pie Chart
actual_counts = df["actual"].value_counts()
axes[1, 1].pie(actual_counts.values,
               labels=actual_counts.index,
               autopct="%1.1f%%",
               colors=["mediumseagreen", "tomato"],
               startangle=90)
axes[1, 1].set_title("Actual Sentiment Split (Dataset)")

# Chart 6 — WordCloud of Positive Reviews
positive_text = " ".join(df[df["vader_sentiment"] == "Positive"]["cleaned_review"])
stop_words = set(stopwords.words("english"))
wordcloud = WordCloud(width=600, height=400,
                      background_color="white",
                      stopwords=stop_words,
                      colormap="Greens").generate(positive_text)
axes[1, 2].imshow(wordcloud, interpolation="bilinear")
axes[1, 2].axis("off")
axes[1, 2].set_title("Most Common Words in Positive Reviews")

plt.tight_layout()
plt.savefig("sentiment_dashboard.png", dpi=150)
plt.show()
print("  Dashboard saved as sentiment_dashboard.png")
print("\nAll done! ✅")
print("\nFiles created:")
print("  📄 imdb_reviews.csv             — raw dataset")
print("  📄 imdb_sentiment_results.csv   — results with sentiment labels")
print("  📊 sentiment_dashboard.png      — visualization dashboard")
