import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection setup
username = 'postgres'
password = 'somilkumar'
host = 'localhost'
port = '5432'
database = 'saas_churn_project'

# Create connection
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load data from the churn_data table
query = "SELECT * FROM churn_data"
df = pd.read_sql(query, engine)

print("\nPreview of raw data:")
print(df.head())

# Step 1: Handle missing values

# Numeric columns with median
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
df['UserRating'] = df['UserRating'].fillna(df['UserRating'].median())

# Categorical columns with mode
cat_cols = ['SubscriptionType', 'PaymentMethod', 'DeviceRegistered',
            'GenrePreference', 'Gender', 'SubtitlesEnabled']

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Final missing values check
print("\n Missing values handled. Verifying:\n")
print(df.isnull().sum())

# Optional: print cleaned shape
print(f"\n Cleaned data shape: {df.shape}")

print("\nColumns after lowercase transformation:")
print(df.columns.tolist())

# Save cleaned data back to PostgreSQL
df.to_sql('cleaned_churn_data', engine, if_exists='replace', index=False)

print("\n Cleaned data saved to table 'cleaned_churn_data'")