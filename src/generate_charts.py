"""
generate_charts.py
--------------------
Reads the cleaned dataset and regenerates every chart used in the
analysis into reports/figures/.

Usage:
    python src/generate_charts.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import seaborn as sns

DATA_PATH = "data/processed/retail_sales_cleaned.csv"
FIG_DIR = "reports/figures"

PALETTE = ["#2E5266", "#6E8898", "#9FB8AD", "#D7C9AA", "#F4A259"]


def money(x, pos):
    return f"${x:,.0f}"


def setup_style():
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.dpi"] = 130
    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.titlesize"] = 13


def monthly_trend(df):
    monthly = df[df["YearMonth"] < "2024-01"].groupby("YearMonth")["Total Amount"].sum()
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(monthly.index, monthly.values, marker="o", color=PALETTE[0], linewidth=2.5)
    ax.fill_between(monthly.index, monthly.values, color=PALETTE[0], alpha=0.08)
    ax.set_title("Monthly Revenue Trend (2023)")
    ax.set_ylabel("Revenue")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money))
    fig.autofmt_xdate(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/01_monthly_trend.png", bbox_inches="tight")
    plt.close()


def revenue_by_category(df):
    cat = df.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(cat.index, cat.values, color=PALETTE[:3])
    ax.set_title("Total Revenue by Product Category")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money))
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/02_revenue_by_category.png", bbox_inches="tight")
    plt.close()


def revenue_by_gender(df):
    gender = df.groupby("Gender")["Total Amount"].sum()
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.pie(gender.values, labels=gender.index, autopct="%1.1f%%",
           colors=[PALETTE[0], PALETTE[4]], startangle=90,
           wedgeprops=dict(width=0.4, edgecolor="white"))
    ax.set_title("Revenue Share by Gender")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/03_revenue_by_gender.png", bbox_inches="tight")
    plt.close()


def age_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.histplot(df["Age"], bins=20, color=PALETTE[0], kde=True, edgecolor="white", ax=ax)
    ax.set_title("Customer Age Distribution")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/04_age_distribution.png", bbox_inches="tight")
    plt.close()


def revenue_by_age_group(df):
    agegrp = df.groupby("Age Group", observed=True)["Total Amount"].sum()
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.bar(agegrp.index.astype(str), agegrp.values, color=PALETTE[1])
    ax.set_title("Total Revenue by Age Group")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money))
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/05_revenue_by_agegroup.png", bbox_inches="tight")
    plt.close()


def revenue_by_weekday(df):
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = df.groupby("Weekday")["Total Amount"].sum().reindex(order)
    colors = [PALETTE[4] if d in ["Saturday", "Sunday"] else PALETTE[0] for d in order]
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.bar(weekday.index, weekday.values, color=colors)
    ax.set_title("Total Revenue by Day of Week")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money))
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/06_revenue_by_weekday.png", bbox_inches="tight")
    plt.close()


def category_by_gender(df):
    gc = df.groupby(["Product Category", "Gender"])["Total Amount"].sum().unstack()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    gc.plot(kind="bar", ax=ax, color=[PALETTE[0], PALETTE[4]])
    ax.set_title("Revenue by Category and Gender")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(money))
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/07_category_gender.png", bbox_inches="tight")
    plt.close()


def correlation_heatmap(df):
    corr = df[["Age", "Quantity", "Price per Unit", "Total Amount"]].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, fmt=".2f", square=True, ax=ax)
    ax.set_title("Correlation Between Numeric Variables")
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/08_correlation_heatmap.png", bbox_inches="tight")
    plt.close()


def main():
    setup_style()
    df = pd.read_csv(DATA_PATH)
    monthly_trend(df)
    revenue_by_category(df)
    revenue_by_gender(df)
    age_distribution(df)
    revenue_by_age_group(df)
    revenue_by_weekday(df)
    category_by_gender(df)
    correlation_heatmap(df)
    print(f"All 8 charts written to {FIG_DIR}/")


if __name__ == "__main__":
    main()
