"""
clean_data.py
--------------
Loads the raw retail sales CSV, runs data-quality checks, cleans it, and
writes the processed output to data/processed/.

Usage:
    python src/clean_data.py
"""
import pandas as pd

RAW_PATH = "data/raw/retail_sales_dataset.csv"
OUT_PATH = "data/processed/retail_sales_cleaned.csv"


def load_data(path: str = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def run_quality_checks(df: pd.DataFrame) -> None:
    print("Missing values per column:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    mismatches = df[df["Total Amount"] != df["Quantity"] * df["Price per Unit"]]
    print("Rows where Total Amount != Quantity x Price per Unit:", len(mismatches))


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])
    df["Customer ID"] = df["Customer ID"].str.strip().str.upper()
    df["Gender"] = df["Gender"].str.strip().str.title()
    df["Product Category"] = df["Product Category"].str.strip().str.title()
    df = df.drop_duplicates().dropna()
    return df


def flag_outliers(df: pd.DataFrame, cols=("Age", "Quantity", "Price per Unit", "Total Amount")):
    for col in cols:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        n_outliers = len(df[(df[col] < lower) | (df[col] > upper)])
        print(f"{col}: {n_outliers} outliers (valid range {lower:.1f} to {upper:.1f})")


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Month"] = df["Date"].dt.month_name()
    df["MonthNum"] = df["Date"].dt.month
    df["Weekday"] = df["Date"].dt.day_name()
    df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    bins = [17, 25, 35, 45, 55, 65]
    labels = ["18-25", "26-35", "36-45", "46-55", "56-64"]
    df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels, include_lowest=True)
    return df


def main():
    df = load_data()
    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns\n")

    run_quality_checks(df)
    df = clean(df)
    flag_outliers(df)
    df = add_features(df)

    df.to_csv(OUT_PATH, index=False)
    print(f"\nSaved cleaned dataset -> {OUT_PATH}  ({df.shape[0]} rows)")


if __name__ == "__main__":
    main()
