# 📚 Web Scraping — Books Dataset
## CodeAlpha Data Analytics Internship — Task 1

## 📌 Project Overview
This project scrapes book data from [books.toscrape.com](https://books.toscrape.com)
using Python, BeautifulSoup, and Pandas. The data is then cleaned and analyzed
to extract meaningful insights about book prices and ratings.

## 📊 Data Collected
- Book Title
- Price (£)
- Star Rating (1–5)
- Availability

## 🔍 Key Findings
- Scraped 250 books across 5 pages
- Average book price: ~£35
- Price range: £10 – £60
- Ratings are fairly evenly distributed across 1–5 stars

## 🛠 Libraries Used
- `requests` — fetch web pages
- `beautifulsoup4` — parse HTML
- `pandas` — store and clean data
- `matplotlib` — create charts

## 📁 File Structure
```
CodeAlpha_WebScraping/
├── main.py             ← runs everything in one go
├── scraper.py          ← scraping only
├── cleaning.py         ← cleaning only
├── analysis.py         ← analysis and charts
├── books_data.csv      ← raw scraped data
├── books_cleaned.csv   ← cleaned data
├── analysis_charts.png ← output charts
└── README.md
```

## ▶️ How to Run

### Install dependencies
```bash
pip install requests beautifulsoup4 pandas matplotlib
```

### Run the full project
```bash
python main.py
```

### Or run step by step
```bash
python scraper.py
python cleaning.py
python analysis.py
```

## 📷 Output Charts
The project generates two charts:
1. **Price Distribution** — histogram of book prices
2. **Books per Rating** — bar chart of star ratings

---
Made with ❤️ as part of CodeAlpha Data Analytics Internship
