import pandas as pd

# Load the dataset
file_path = "channels.csv"  # Update with correct path
df = pd.read_csv(file_path)

print("\n INITIAL DATA OVERVIEW")
print(df.info())
print("\nFirst 5 Rows (Before Cleaning):")
print(df.head())

# Check for missing values before cleaning
print("\n MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Drop irrelevant columns
columns_to_drop = ["profile_url", "picture_url", "extra_column_if_any"]  # Add/remove columns as needed
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

print("\n Dropped Irrelevant Columns: Profile URL, Picture URL, Extra Column If Any")
print(df.head())

# Handle missing values
df.fillna({'category_name': 'Unknown', 'country': 'Unknown', 'followers': 0, 'engagement_rate': 0}, inplace=True)

print("\n Missing Values Replaced (Check Sample Rows):")
print(df.sample(5))

# Convert join_date to datetime format
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

print("\n Converted 'join_date' to Datetime Format:")
print(df[['join_date']].sample(5))

# Ensure followers is numeric
if 'followers' in df.columns:
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce').fillna(0).astype(int)

print("\n Converted 'followers' to Numeric Format:")
print(df[['followers']].describe())

# Standardize category names
if 'category_name' in df.columns:
    df['category_name'] = df['category_name'].str.title().str.strip()

print("\n Standardized 'category_name' Column:")
print(df['category_name'].value_counts().head())

# Save cleaned dataset as Excel file
cleaned_file_path = "cleaned_channels.xlsx"
df.to_excel(cleaned_file_path, index=False, engine='openpyxl')

print("\n DATA CLEANING COMPLETED! Cleaned dataset saved at:", cleaned_file_path)
print("\n FINAL DATA OVERVIEW")
print(df.info())
print("\n First 5 Rows (After Cleaning):")
print(df.head())
