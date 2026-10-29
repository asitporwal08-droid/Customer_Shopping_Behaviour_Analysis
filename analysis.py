
import pandas as pd
from pathlib import Path

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "shopping_trends_updated.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

print("=" * 50)
print("CUSTOMER SHOPPING BEHAVIOUR ANALYSIS")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head().to_string(index=False))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nAnalysis completed successfully!")


# STEP 7: DATA QUALITY CHECKS

print("\n" + "=" * 50)
print("DATA QUALITY CHECKS")
print("=" * 50)

# Check dataset size
print("\nTotal Rows:", len(df))
print("Total Columns:", len(df.columns))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().to_string())

# Check duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())

# Check unique customers
if "Customer ID" in df.columns:
    print("Unique Customers:", df["Customer ID"].nunique())

# Check purchase amount
if "Purchase Amount (USD)" in df.columns:
    print("\nPurchase Amount Summary:")
    print(df["Purchase Amount (USD)"].describe())

# Check categories
if "Category" in df.columns:
    print("\nProduct Categories:")
    print(df["Category"].value_counts().to_string())

print("\nData quality check completed!")


# STEP 8: DATA CLEANING

clean_df = df.copy()

# Remove duplicate rows
clean_df = clean_df.drop_duplicates()

# Remove rows that have no values in essential columns
essential_columns = [
    col for col in ["Customer ID", "Purchase Amount (USD)", "Category"]
    if col in clean_df.columns
]

if essential_columns:
    clean_df = clean_df.dropna(subset=essential_columns)

# Save cleaned dataset
OUTPUT_FILE = PROJECT_DIR / "data" / "customer_shopping_cleaned.csv"
clean_df.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 50)
print("DATA CLEANING RESULTS")
print("=" * 50)
print("Original rows:", len(df))
print("Cleaned rows:", len(clean_df))
print("Rows removed:", len(df) - len(clean_df))
print("Cleaned file saved to:", OUTPUT_FILE)


# STEP 9: BUSINESS ANALYSIS

print("\n" + "=" * 50)
print("CUSTOMER SHOPPING BUSINESS ANALYSIS")
print("=" * 50)

# Total revenue
if "Purchase Amount (USD)" in clean_df.columns:
    print("\nTotal Revenue: $", round(
        clean_df["Purchase Amount (USD)"].sum(), 2
    ))

    print("Average Purchase: $", round(
        clean_df["Purchase Amount (USD)"].mean(), 2
    ))

# Gender analysis
if "Gender" in clean_df.columns:
    print("\nPurchases by Gender:")
    print(clean_df["Gender"].value_counts().to_string())

# Top selling categories by transaction count
if "Category" in clean_df.columns:
    print("\nPurchases by Category:")
    print(clean_df["Category"].value_counts().to_string())

# Most popular payment methods
if "Payment Method" in clean_df.columns:
    print("\nPayment Methods:")
    print(clean_df["Payment Method"].value_counts().to_string())

# Average purchase by category
if all(col in clean_df.columns for col in
       ["Category", "Purchase Amount (USD)"]):
    print("\nAverage Purchase by Category:")
    print(
        clean_df.groupby("Category")["Purchase Amount (USD)"]
        .mean().round(2).sort_values(ascending=False).to_string()
    )

print("\nBusiness analysis completed!")


# STEP 10: BUSINESS VISUALIZATIONS

import matplotlib.pyplot as plt

# Category-wise purchase count
if "Category" in clean_df.columns:
    category_counts = clean_df["Category"].value_counts()

    plt.figure(figsize=(9, 5))
    category_counts.plot(kind="bar")
    plt.title("Customer Purchases by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(PROJECT_DIR / "data" / "category_purchases.png")
    plt.show()

# Payment method distribution
if "Payment Method" in clean_df.columns:
    payment_counts = clean_df["Payment Method"].value_counts()

    plt.figure(figsize=(8, 5))
    payment_counts.plot(kind="bar")
    plt.title("Purchases by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(PROJECT_DIR / "data" / "payment_methods.png")
    plt.show()

print("Charts saved in the data folder!")

