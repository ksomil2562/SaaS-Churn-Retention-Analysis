import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
username = 'postgres'
password = 'somilkumar'
host = 'localhost'
port = '5432'
database = 'saas_churn_project'

# Create engine
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load cleaned data
df = pd.read_sql("SELECT * FROM cleaned_churn_data", engine)

# Export to CSV
df.to_csv("cleaned_churn_data.csv", index=False)

print(" Exported 'cleaned_churn_data.csv' successfully!")
