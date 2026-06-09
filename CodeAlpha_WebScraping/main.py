import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# =====================
# STEP 1: SCRAPING
# =====================
print("=" * 40)
print("STEP 1: Scraping data...")
print("=" * 40)

books = []

for page in range(1, 6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        availability = book.find("p", class_="availability").text.strip()

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    print(f"  Page {page} scraped ✓")

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)
print(f"  Raw data saved! Total books: {len(df)}\n")

# =====================
# STEP 2: CLEANING
# =====================
print("=" * 40)
print("STEP 2: Cleaning data...")
print("=" * 40)

df["Price"] = df["Price"].apply(lambda x: re.sub(r"[^\d.]", "", x)).astype(float)

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating"] = df["Rating"].map(rating_map)

df["Title"] = df["Title"].str.strip()
df = df.dropna()

df.to_csv("books_cleaned.csv", index=False)
print("  Data cleaned and saved!\n")

# =====================
# STEP 3: ANALYSIS
# =====================
print("=" * 40)
print("STEP 3: Analysis")
print("=" * 40)

print(f"Average Price:   £{df['Price'].mean():.2f}")
print(f"Cheapest Book:   £{df['Price'].min()} → {df.loc[df['Price'].idxmin(), 'Title']}")
print(f"Most Expensive:  £{df['Price'].max()} → {df.loc[df['Price'].idxmax(), 'Title']}")
print(f"Average Rating:  {df['Rating'].mean():.2f} stars")

# =====================
# STEP 4: CHARTS
# =====================
print("\n" + "=" * 40)
print("STEP 4: Creating charts...")
print("=" * 40)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df["Price"], bins=20, color="steelblue", edgecolor="black")
axes[0].set_title("Book Price Distribution", fontsize=14)
axes[0].set_xlabel("Price (£)")
axes[0].set_ylabel("Number of Books")

df["Rating"].value_counts().sort_index().plot(
    kind="bar", color="coral", edgecolor="black", ax=axes[1]
)
axes[1].set_title("Books per Star Rating", fontsize=14)
axes[1].set_xlabel("Star Rating")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig("analysis_charts.png", dpi=150)
plt.show()
print("  Charts saved as analysis_charts.png")
print("\nAll done! ✅")
