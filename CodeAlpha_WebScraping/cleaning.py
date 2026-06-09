import pandas as pd
import re

# Load raw data
df = pd.read_csv("books_data.csv")
print("Before cleaning:")
print(df.head())
print(df.dtypes)

# --- Clean Price ---
# Remove hidden characters and currency symbol
df["Price"] = df["Price"].apply(lambda x: re.sub(r"[^\d.]", "", x)).astype(float)

# --- Clean Rating ---
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

# --- Clean Title ---
df["Title"] = df["Title"].str.strip()

# --- Drop missing values ---
df = df.dropna()

# --- Save cleaned data ---
df.to_csv("books_cleaned.csv", index=False)

print("\nAfter cleaning:")
print(df.head())
print(f"\nClean data saved! Total books: {len(df)}")
