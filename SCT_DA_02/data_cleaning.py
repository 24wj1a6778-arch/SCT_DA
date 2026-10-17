
import pandas as pd
from pathlib import Path

# 1. Load the dataset
folder = Path(__file__).resolve().parent
input_file = folder / "raw_data.csv"
output_file = folder / "cleaned_data.csv"

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 2. Clean column names
df.columns = df.columns.str.strip()

# 3. Identify missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 4. Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicates)

# 5. Convert data types
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(
        df["Order Date"], errors="coerce"
    )

if "Ship Date" in df.columns:
    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"], errors="coerce"
    )

if "Sales" in df.columns:
    df["Sales"] = pd.to_numeric(
        df["Sales"], errors="coerce"
    )

# 6. Handle missing values
# Fill missing text/category values with "Unknown"
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna("Unknown")

# Fill missing numeric values with the median
for col in df.select_dtypes(include="number").columns:
    if df[col].isnull().any():
        median_value = df[col].median()
        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)

# Drop rows missing essential analysis fields
essential_columns = [
    col for col in ["Order ID", "Order Date", "Sales"]
    if col in df.columns
]

if essential_columns:
    df = df.dropna(subset=essential_columns)

# 7. Check the cleaned dataset
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)

# 8. Export cleaned data to a new CSV file
df.to_csv(output_file, index=False)

print("\nData cleaning completed successfully!")
print("Cleaned file saved to:", output_file)
