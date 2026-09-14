# Retail Sales Analysis

An end-to-end retail sales analysis using Python to identify revenue trends, product performance, customer segments, and purchasing patterns across **1,000 transactions**.

## Business Objective

The goal was to answer:

> **What's selling, who's buying, when does revenue perform best, and what actions could the business take based on the data?**

The project covers data quality validation, cleaning, feature engineering, exploratory analysis, visualization, and business recommendations.

## Key Results

| Metric | Result |
|---|---:|
| Total Revenue | **$456,000** |
| Transactions | **1,000** |
| Average Order Value | **$456.00** |
| Unique Customers | **1,000** |

### Key Insights

- **Revenue is evenly distributed across product categories.** Electronics generated $156,905, Clothing $155,580, and Beauty $143,515, indicating no single category dominates sales.
- **Saturday was the strongest sales day**, generating $78,815 in revenue, while Thursday was the weakest at $53,835.
- **May was the strongest month** at $53,150, while September was the weakest at $23,620. More years of data would be required to determine whether this reflects genuine seasonality.
- **Customers aged 46–55 generated the highest total revenue** ($100,690), while customers aged 18–25 had the highest average order value ($500.30).
- **Gender showed little difference in spending behavior.** Female customers generated 51% of revenue versus 49% for male customers, with nearly identical average order values.
- **The dataset contains one transaction per customer**, meaning repeat-purchase behavior and customer retention cannot be evaluated from this dataset.

## Business Recommendations

Based on the available data:

1. **Prioritize Saturday trading activity** through promotions, staffing, and inventory planning.
2. **Investigate the May/September revenue gap** using additional years of data before making seasonal decisions.
3. **Avoid heavily gendered merchandising strategies**, as spending and category preferences are relatively balanced.
4. **Investigate the 18–25 segment further**, as it has the highest average order value despite generating less total revenue than the 46–55 segment.
5. **Collect repeat-purchase data** to enable customer retention, lifetime value, and cohort analysis.

## Data & Methodology

The dataset contains **1,000 retail transactions** from January 2023 to January 2024.

Analysis included:

- Missing-value and duplicate checks
- Transaction consistency validation
- Outlier detection using the IQR method
- Data type and text normalization
- Feature engineering for month, weekday, year-month, and age groups
- Exploratory data analysis
- Revenue and customer segmentation
- Data visualization

The source dataset contained **no missing values, duplicate rows, or Total Amount calculation errors**.

## Repository Structure

```text
retail-sales-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── retail_sales_analysis.ipynb
├── reports/
│   └── figures/
├── src/
│   ├── clean_data.py
│   └── generate_charts.py
├── requirements.txt
└── README.md
```

## Tech Stack

- **Python**
- **Pandas / NumPy** — data manipulation and analysis
- **Matplotlib / Seaborn** — visualization
- **Jupyter Notebook** — exploratory analysis
- **Git / GitHub** — version control


