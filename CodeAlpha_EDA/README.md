# 🚢 Exploratory Data Analysis — Titanic Dataset
## CodeAlpha Data Analytics Internship — Task 2

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on the famous Titanic dataset.
The goal is to explore patterns, understand the data structure, and extract meaningful
insights about passenger survival using statistics and visualizations.

## ❓ Key Questions Explored
1. What was the overall survival rate?
2. Did gender affect chances of survival?
3. Did passenger class affect survival?
4. What was the age distribution of passengers?
5. How were ticket fares distributed?
6. Is there a relationship between age, fare, and survival?

## 🔍 Key Findings
- Overall survival rate was ~38%
- Women had a much higher survival rate (~74%) than men (~19%)
- 1st class passengers survived more than 3rd class passengers
- Most passengers were between 20–40 years old
- Fare prices were heavily right-skewed (most paid low fares)

## 🛠 Libraries Used
- `pandas` — data loading and manipulation
- `matplotlib` — base charts
- `seaborn` — statistical visualizations

## 📁 File Structure
```
CodeAlpha_EDA/
├── main.py                  ← runs everything
├── titanic.csv              ← raw dataset
├── titanic_cleaned.csv      ← cleaned dataset
├── titanic_eda_charts.png   ← output charts
└── README.md
```

## ▶️ How to Run

### Install dependencies
```bash
pip install pandas matplotlib seaborn
```

### Run the project
```bash
python main.py
```

## 📷 Output
The project generates 6 charts:
1. Survival Count
2. Survival Rate by Gender
3. Survival Rate by Passenger Class
4. Age Distribution
5. Fare Distribution
6. Age vs Fare scatter plot (colored by survival)

