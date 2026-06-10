# 🛒 Data Visualization — Superstore Sales Dashboard
## CodeAlpha Data Analytics Internship — Task 3

## 📌 Project Overview
This project creates a comprehensive data visualization dashboard using the
Superstore Sales dataset. The goal is to transform raw sales data into clear,
insightful charts that tell a compelling business story.

## ❓ Key Questions Visualized
1. Which product category generates the most sales?
2. Which region is the most profitable?
3. How have sales trended over time?
4. What are the top 10 best-selling sub-categories?
5. Is there a relationship between sales and profit?
6. How are sales distributed across all orders?

## 🔍 Key Insights
- Technology is the highest revenue category
- The West region generates the most profit
- Sales show a consistent upward trend over the years
- Phones and Chairs are top sub-categories by sales
- Some high-sales products actually generate negative profit (loss leaders)

## 🛠 Libraries Used
- `pandas` — data loading and manipulation
- `matplotlib` — static chart creation
- `seaborn` — statistical visualizations
- `plotly` — interactive charts and dashboard

## 📁 File Structure
```
CodeAlpha_DataVisualization/
├── main.py                      ← runs everything
├── superstore.csv               ← raw dataset
├── superstore_cleaned.csv       ← cleaned dataset
├── superstore_dashboard.png     ← static 6-chart dashboard
├── interactive_dashboard.html   ← interactive dashboard (open in browser)
├── interactive_scatter.html     ← interactive scatter plot (open in browser)
└── README.md
```

## ▶️ How to Run

### Install dependencies
```bash
pip install pandas matplotlib seaborn plotly
```

### Run the project
```bash
python main.py
```

## 📷 Output
The project generates:
1. **superstore_dashboard.png** — static 6-chart dashboard with:
   - Total Sales by Category
   - Total Profit by Region
   - Monthly Sales Trend
   - Top 10 Sub-Categories by Sales
   - Sales vs Profit scatter plot
   - Sales Distribution histogram

2. **interactive_dashboard.html** — interactive dashboard (open in any browser):
   - Hover over charts for exact values
   - Zoom in/out on any chart
   - Click legend to filter data

3. **interactive_scatter.html** — interactive Sales vs Profit scatter:
   - Hover to see Sub-Category and Region details
   - Filter by Category using the legend

---
Made with ❤️ as part of CodeAlpha Data Analytics Internship
