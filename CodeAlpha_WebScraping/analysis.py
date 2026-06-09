import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("books_cleaned.csv")

# --- Price Analysis ---
print("=== PRICE ANALYSIS ===")
print(f"Average Price:   £{df['Price'].mean():.2f}")
print(f"Cheapest Price:  £{df['Price'].min()} → {df.loc[df['Price'].idxmin(), 'Title']}")
print(f"Most Expensive:  £{df['Price'].max()} → {df.loc[df['Price'].idxmax(), 'Title']}")

# --- Rating Analysis ---
print("\n=== RATING ANALYSIS ===")
print(f"Average Rating: {df['Rating'].mean():.2f}")
print(f"Most Common Rating: {df['Rating'].mode()[0]} stars")
print("\nRatings Breakdown:")
print(df["Rating"].value_counts().sort_index())

# --- Best Value Books ---
print("\n=== BEST VALUE BOOKS (Rating >= 4 & Price < £20) ===")
best_value = df[(df["Rating"] >= 4) & (df["Price"] < 20)]
print(best_value[["Title", "Price", "Rating"]].to_string(index=False))

# --- Charts ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: Price Distribution
axes[0].hist(df["Price"], bins=20, color="steelblue", edgecolor="black")
axes[0].set_title("Book Price Distribution", fontsize=14)
axes[0].set_xlabel("Price (£)")
axes[0].set_ylabel("Number of Books")

# Chart 2: Books per Rating
df["Rating"].value_counts().sort_index().plot(
    kind="bar", color="coral", edgecolor="black", ax=axes[1]
)
axes[1].set_title("Number of Books per Star Rating", fontsize=14)
axes[1].set_xlabel("Star Rating")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig("analysis_charts.png", dpi=150)
plt.show()
print("\nCharts saved as analysis_charts.png")
