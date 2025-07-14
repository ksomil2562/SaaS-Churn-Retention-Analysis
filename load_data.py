import pandas as pd
from sqlalchemy import create_engine

# Replace placeholders with your actual PostgreSQL credentials
username = 'postgres'
password = 'somilkumar'   # use the password you set
host = 'localhost'
port = '5432'
database = 'saas_churn_project'   # or whatever DB name you created


# Create connection
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Read churn_data table
df = pd.read_sql('SELECT * FROM churn_data', engine)

# Display first few rows
print(df.head())
