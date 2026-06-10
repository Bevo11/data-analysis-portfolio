import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =====================
# STEP 1: LOAD DATA
# =====================
print("=" * 40)
print("STEP 1: Loading Superstore dataset...")
print("=" * 40)

# Load from local CSV file (place superstore.csv in the same folder as this script)
df = pd.read_csv("superstore.csv", encoding="latin-1")
print(f"  Dataset loaded! Shape: {df.shape}")
print(df.head())

# =====================
# STEP 2: CLEAN DATA
# =====================
print("\n" + "=" * 40)
print("STEP 2: Cleaning data...")
print("=" * 40)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

print(f"  Missing values:\n{df.isnull().sum()}")
df.to_csv("superstore_cleaned.csv", index=False)
print("  Cleaned data saved!")

# =====================
# STEP 3: ANALYSIS
# =====================
print("\n" + "=" * 40)
print("STEP 3: Key Analysis")
print("=" * 40)

print(f"Total Sales:   ${df['Sales'].sum():,.2f}")
print(f"Total Profit:  ${df['Profit'].sum():,.2f}")
print(f"Total Orders:  {len(df)}")
print(f"\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print(f"\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

# =====================
# STEP 4: STATIC CHARTS
# =====================
print("\n" + "=" * 40)
print("STEP 4: Creating static charts...")
print("=" * 40)

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle("Superstore Sales Dashboard", fontsize=18, fontweight="bold")

# Chart 1 — Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values()
axes[0, 0].barh(category_sales.index, category_sales.values,
                color=["steelblue", "coral", "mediumseagreen"])
axes[0, 0].set_title("Total Sales by Category")
axes[0, 0].set_xlabel("Total Sales ($)")
for i, v in enumerate(category_sales.values):
    axes[0, 0].text(v + 1000, i, f"${v:,.0f}", va="center", fontsize=9)

# Chart 2 — Profit by Region
region_profit = df.groupby("Region")["Profit"].sum().sort_values()
colors = ["red" if x < 0 else "mediumseagreen" for x in region_profit.values]
axes[0, 1].bar(region_profit.index, region_profit.values, color=colors, edgecolor="black")
axes[0, 1].set_title("Total Profit by Region")
axes[0, 1].set_ylabel("Profit ($)")
axes[0, 1].tick_params(axis="x", rotation=0)

# Chart 3 — Monthly Sales Trend
monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum().reset_index()
monthly_sales["Date"] = pd.to_datetime(monthly_sales[["Year", "Month"]].assign(Day=1))
axes[0, 2].plot(monthly_sales["Date"], monthly_sales["Sales"],
                color="steelblue", linewidth=2)
axes[0, 2].set_title("Monthly Sales Trend Over Time")
axes[0, 2].set_xlabel("Date")
axes[0, 2].set_ylabel("Sales ($)")
axes[0, 2].tick_params(axis="x", rotation=30)

# Chart 4 — Top 10 Sub-Categories by Sales
top_sub = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
axes[1, 0].bar(top_sub.index, top_sub.values, color="mediumpurple", edgecolor="black")
axes[1, 0].set_title("Top 10 Sub-Categories by Sales")
axes[1, 0].set_ylabel("Sales ($)")
axes[1, 0].tick_params(axis="x", rotation=45)

# Chart 5 — Sales vs Profit by Category
colors_map = {"Furniture": "red", "Office Supplies": "steelblue", "Technology": "green"}
for category, group in df.groupby("Category"):
    axes[1, 1].scatter(group["Sales"], group["Profit"],
                       alpha=0.4, label=category,
                       color=colors_map[category], s=20)
axes[1, 1].set_title("Sales vs Profit by Category")
axes[1, 1].set_xlabel("Sales ($)")
axes[1, 1].set_ylabel("Profit ($)")
axes[1, 1].legend()
axes[1, 1].axhline(0, color="black", linewidth=0.8, linestyle="--")

# Chart 6 — Sales Distribution
axes[1, 2].hist(df["Sales"], bins=50, color="coral", edgecolor="black")
axes[1, 2].set_title("Sales Distribution")
axes[1, 2].set_xlabel("Sales ($)")
axes[1, 2].set_ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("superstore_dashboard.png", dpi=150)
plt.show()
print("  Dashboard saved as superstore_dashboard.png")

# =====================
# STEP 5: INTERACTIVE CHARTS (PLOTLY)
# =====================
print("\n" + "=" * 40)
print("STEP 5: Creating interactive charts...")
print("=" * 40)

fig_interactive = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Sales by Category",
        "Profit by Region",
        "Monthly Sales Trend",
        "Top 10 Sub-Categories by Sales"
    )
)

# Interactive Chart 1 — Sales by Category
cat_sales = df.groupby("Category")["Sales"].sum().reset_index()
fig_interactive.add_trace(
    go.Bar(x=cat_sales["Category"], y=cat_sales["Sales"],
           marker_color=["steelblue", "coral", "mediumseagreen"],
           name="Sales by Category", showlegend=False),
    row=1, col=1
)

# Interactive Chart 2 — Profit by Region
reg_profit = df.groupby("Region")["Profit"].sum().reset_index()
bar_colors = ["red" if x < 0 else "mediumseagreen" for x in reg_profit["Profit"]]
fig_interactive.add_trace(
    go.Bar(x=reg_profit["Region"], y=reg_profit["Profit"],
           marker_color=bar_colors,
           name="Profit by Region", showlegend=False),
    row=1, col=2
)

# Interactive Chart 3 — Monthly Sales Trend
monthly = df.groupby(["Year", "Month"])["Sales"].sum().reset_index()
monthly["Date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(Day=1))
fig_interactive.add_trace(
    go.Scatter(x=monthly["Date"], y=monthly["Sales"],
               mode="lines", line=dict(color="steelblue", width=2),
               name="Monthly Sales", showlegend=False),
    row=2, col=1
)

# Interactive Chart 4 — Top 10 Sub-Categories
top10 = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
fig_interactive.add_trace(
    go.Bar(x=top10["Sub-Category"], y=top10["Sales"],
           marker_color="mediumpurple",
           name="Top Sub-Categories", showlegend=False),
    row=2, col=2
)

fig_interactive.update_layout(
    title_text="Superstore Sales — Interactive Dashboard",
    title_font_size=20,
    height=700,
    template="plotly_white"
)

fig_interactive.write_html("interactive_dashboard.html")
print("  Interactive dashboard saved as interactive_dashboard.html")

# Bonus: Interactive Scatter — Sales vs Profit
fig_scatter = px.scatter(
    df, x="Sales", y="Profit",
    color="Category",
    hover_data=["Sub-Category", "Region"],
    title="Sales vs Profit — Hover for Details",
    template="plotly_white",
    opacity=0.6
)
fig_scatter.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.5)
fig_scatter.write_html("interactive_scatter.html")
print("  Interactive scatter saved as interactive_scatter.html")

print("\nAll done! ✅")
print("\nFiles created:")
print("  📊 superstore_dashboard.png   — static charts")
print("  🌐 interactive_dashboard.html — interactive dashboard (open in browser)")
print("  🌐 interactive_scatter.html   — interactive scatter plot (open in browser)")
