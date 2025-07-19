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

# Load data
query = "SELECT * FROM churn_data"
df = pd.read_sql(query, engine)

print("\nPreview of raw data:")
print(df.head())

# Handle missing values
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
df['UserRating'] = df['UserRating'].fillna(df['UserRating'].median())

cat_cols = ['SubscriptionType', 'PaymentMethod', 'DeviceRegistered',
            'GenrePreference', 'Gender', 'SubtitlesEnabled']
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Final check
print("\nMissing values handled:\n", df.isnull().sum())
print(f"\nCleaned data shape: {df.shape}")

# Save cleaned data
df.to_sql('cleaned_churn_data', engine, if_exists='replace', index=False)
print("\n Cleaned data saved to 'cleaned_churn_data'")

# ----------- SCALING TO 10,000 USERS ------------------

# ✅ Sample 10,000 rows with replacement from cleaned data
scaled_df = df.sample(n=10000, replace=True, random_state=42).reset_index(drop=True)

# ✅ Multiply MonthlyCharges by 15 to simulate premium pricing
scaled_df['MonthlyCharges'] = scaled_df['MonthlyCharges'] * 15

# ✅ Save to PostgreSQL
scaled_df.to_sql('scaled_churn_data', engine, if_exists='replace', index=False)
print(" Scaled data (10,000 users with boosted MonthlyCharges) saved to 'scaled_churn_data'")
