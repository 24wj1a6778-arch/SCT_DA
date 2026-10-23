#  Data Cleaning and Preparation

A beginner-friendly data analytics project demonstrating how to clean and prepare a CSV dataset using **Python** and **Pandas**.

##  Project Overview

The goal is to improve data quality before analysis by inspecting missing values, removing duplicate records, converting columns to suitable data types, handling missing values, and exporting the cleaned dataset to a new CSV file.

This project uses the Superstore dataset (`raw_data.csv`).

##  Objectives

- Load a CSV dataset into a Pandas DataFrame.
- Inspect the dataset and identify missing values.
- Detect and remove duplicate rows.
- Convert columns to appropriate data types, such as order dates and sales values.
- Handle missing values using suitable rules.
- Export the cleaned data to `cleaned_data.csv`.

##  Tools and Technologies

- **Python**
- **Pandas**
- **Visual Studio Code (VS Code)**
- **CSV** input and output files

##  Project Structure

Task02_Data_Cleaning/
├── raw_data.csv          # Original dataset
├── data_cleaning.py      # Data-cleaning script
├── cleaned_data.csv      # Generated output
└── README.md             # Project documentation

##  Requirements

- Python 3
- Pandas

Install Pandas:
```
py -m pip install pandas
```

If `py` is unavailable, use:
```
python -m pip install pandas
```

##  How to Run

1. Clone or download this repository.
2. Place `raw_data.csv` in the same folder as `data_cleaning.py`.
3. Open a terminal in the project folder.
4. Run the script:
   ```
   py data_cleaning.py
   ```
   Or:
   ```
   python data_cleaning.py
   ```
5. Review the terminal output for the dataset shape, missing-value summary, duplicate count, and data types.
6. Open `cleaned_data.csv` in Excel, VS Code, or another CSV viewer.

##  Data-Cleaning Steps

1. **Load data:** Read the source CSV using `pandas.read_csv()`.
2. **Standardize column names:** Remove extra whitespace from column labels.
3. **Inspect missing values:** Count missing values with `DataFrame.isnull().sum()`.
4. **Remove duplicates:** Remove exact duplicate rows using `DataFrame.drop_duplicates()`.
5. **Convert data types:** Parse `Order Date` and `Ship Date` as dates and `Sales` as numeric values when those columns exist.
6. **Handle missing values:** Fill missing text fields with `Unknown` and missing numeric fields with the median where appropriate.
7. **Validate essential fields:** Remove rows that still have missing values in essential fields such as Order ID, Order Date, or Sales.
8. **Export results:** Save the processed data as `cleaned_data.csv` without a CSV index column.

> **Note:** Missing-value strategies should be selected based on the dataset and the meaning of each column. Median imputation is a general example and may not be appropriate for every field.

##  Expected Output
When the script runs successfully, it reports information such as:

- Original and cleaned dataset dimensions
- Missing values before and after cleaning
- Number of duplicate rows removed
- Column data types
- Location of the generated `cleaned_data.csv`
The original dataset remains unchanged; the cleaned data is written to a separate file.

##  Troubleshooting
### `ModuleNotFoundError: No module named 'pandas'`
Install Pandas using the same Python interpreter that runs the script:
```
py -m pip install pandas
```

### The cleaned CSV is not generated
- Confirm `data_cleaning.py` contains the code and has been saved.
- Confirm `raw_data.csv` is in the same directory.
- Run the command from the project folder.
- Read any error message printed in the terminal.


##  Skills Demonstrated
- Data inspection and validation
- Missing-value analysis and handling
- Duplicate detection and removal
- Data type conversion
- CSV input/output
- Python scripting with Pandas

##  Future Improvements
- Add before-and-after data quality summaries.
- Record the number of missing values handled in each column.
- Add configurable cleaning rules for different datasets.
- Add automated checks to validate the cleaned output.
