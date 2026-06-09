import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# STEP 1: LOAD DATA
# =====================
print("=" * 40)
print("STEP 1: Loading Titanic dataset...")
print("=" * 40)

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.to_csv("titanic.csv", index=False)
print(f"  Dataset loaded! Shape: {df.shape}")
print(df.head())

# =====================
# STEP 2: UNDERSTAND
# =====================
print("\n" + "=" * 40)
print("STEP 2: Understanding the data...")
print("=" * 40)
print("\nData Types:")
print(df.dtypes)
print("\nBasic Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# =====================
# STEP 3: CLEAN
# =====================
print("\n" + "=" * 40)
print("STEP 3: Cleaning data...")
print("=" * 40)

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked with most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin (too many missing values)
df = df.drop(columns=["Cabin"])

print("  Missing values after cleaning:")
print(df.isnull().sum())
df.to_csv("titanic_cleaned.csv", index=False)
print("  Cleaned data saved!")

# =====================
# STEP 4: ANALYSIS
# =====================
print("\n" + "=" * 40)
print("STEP 4: Key Analysis")
print("=" * 40)

print(f"\nTotal Passengers:  {len(df)}")
print(f"Survival Rate:     {df['Survived'].mean()*100:.1f}%")
print(f"Average Age:       {df['Age'].mean():.1f} years")
print(f"Average Fare:      £{df['Fare'].mean():.2f}")

print("\nSurvival by Gender:")
print(df.groupby("Sex")["Survived"].mean().apply(lambda x: f"{x*100:.1f}%"))

print("\nSurvival by Class:")
print(df.groupby("Pclass")["Survived"].mean().apply(lambda x: f"{x*100:.1f}%"))

print("\nSurvival by Embarkation Port:")
print(df.groupby("Embarked")["Survived"].mean().apply(lambda x: f"{x*100:.1f}%"))

# =====================
# STEP 5: VISUALIZATIONS
# =====================
print("\n" + "=" * 40)
print("STEP 5: Creating charts...")
print("=" * 40)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Titanic EDA — Key Insights", fontsize=16, fontweight="bold")

# Chart 1 — Survival Count
sns.countplot(x="Survived", data=df, palette="Set2", ax=axes[0, 0])
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xticklabels(["Did Not Survive", "Survived"])
axes[0, 0].set_xlabel("")

# Chart 2 — Survival by Gender
sns.barplot(x="Sex", y="Survived", data=df, palette="Set1", ax=axes[0, 1])
axes[0, 1].set_title("Survival Rate by Gender")
axes[0, 1].set_ylabel("Survival Rate")

# Chart 3 — Survival by Class
sns.barplot(x="Pclass", y="Survived", data=df, palette="Blues_d", ax=axes[0, 2])
axes[0, 2].set_title("Survival Rate by Passenger Class")
axes[0, 2].set_xlabel("Class (1=First, 3=Third)")

# Chart 4 — Age Distribution
axes[1, 0].hist(df["Age"], bins=30, color="steelblue", edgecolor="black")
axes[1, 0].set_title("Age Distribution of Passengers")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Count")

# Chart 5 — Fare Distribution
axes[1, 1].hist(df["Fare"], bins=30, color="coral", edgecolor="black")
axes[1, 1].set_title("Fare Distribution")
axes[1, 1].set_xlabel("Fare (£)")
axes[1, 1].set_ylabel("Count")

# Chart 6 — Age vs Fare colored by Survival
survived = df[df["Survived"] == 1]
not_survived = df[df["Survived"] == 0]
axes[1, 2].scatter(not_survived["Age"], not_survived["Fare"],
                   alpha=0.5, label="Did Not Survive", color="red", s=20)
axes[1, 2].scatter(survived["Age"], survived["Fare"],
                   alpha=0.5, label="Survived", color="green", s=20)
axes[1, 2].set_title("Age vs Fare (by Survival)")
axes[1, 2].set_xlabel("Age")
axes[1, 2].set_ylabel("Fare")
axes[1, 2].legend()

plt.tight_layout()
plt.savefig("titanic_eda_charts.png", dpi=150)
plt.show()
print("  Charts saved as titanic_eda_charts.png")
print("\nAll done! ✅")
