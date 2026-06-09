import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

print("Starting to scrape...")

for page in range(1, 6):  # scrape 5 pages (change to 51 for all pages)
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

    print(f"Page {page} scraped ✓")

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)
print(f"\nDone! Scraped {len(df)} books.")
print(df.head())
