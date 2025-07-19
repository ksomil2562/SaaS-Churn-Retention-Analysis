import pandas as pd
from sqlalchemy import create_engine

# DB connection
username = 'postgres'
password = 'somilkumar'
host = 'localhost'
port = '5432'
database = 'saas_churn_project'
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load scaled data
df = pd.read_sql("SELECT * FROM scaled_churn_data", engine)

# Drop missing revenue values if any (just in case)
df = df.dropna(subset=['MonthlyCharges'])

# Total customers and churn
total_customers = len(df)
churned_customers = df[df['Churn'] == 1]
current_churn_rate = len(churned_customers) / total_customers * 100

print(f"\n Current churn rate: {current_churn_rate:.2f}%")
print(f" Total customers: {total_customers}")
print(f" Churned customers: {len(churned_customers)}")

# ----- Simulation: Retain enough to reduce churn by 9% -----
target_churn_reduction = 0.09  # 9% of total users
retained_count = int(target_churn_reduction * total_customers)

# Randomly retain required number of churned users
retained_users = churned_customers.sample(n=retained_count, random_state=42)

# Revenue gained by retaining them
projected_gain = retained_users['MonthlyCharges'].sum()
churn_reduction_percent = (retained_count / total_customers) * 100

print("\n--- SIMULATION RESULTS ---")
print(f" Retained churned users: {retained_count}")
print(f" Simulated churn reduction: {churn_reduction_percent:.2f}%")
print(f" Projected monthly revenue gain: {projected_gain:,.2f}")
