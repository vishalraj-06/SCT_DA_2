import pandas as pd

# Load dataset
df = pd.read_csv("/content/Global_Superstore2.csv", encoding='latin1')

# Check dataset information
print(df.info())

# Check missing values
missing = df.isnull().sum()
print("\nMissing values:\n")
print(missing)

# Handle missing values only if they exist
for column in df.columns:

    if df[column].isnull().sum() > 0:

        # Numeric columns → fill with mean
        if df[column].dtype in ["int64", "float64"]:
            df[column] = df[column].fillna(df[column].mean())

        # Text columns → fill with "Unknown"
        else:
            df[column] = df[column].fillna("Unknown")

# Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Export cleaned file
df.to_csv("Cleaned_Global_Superstore.csv", index=False)

print("Data cleaning completed successfully.")
