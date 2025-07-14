import pandas as pd
from sqlalchemy import create_engine

# DB connection
username = 'postgres'
password = 'somilkumar'
host = 'localhost'
port = '5432'
database = 'saas_churn_project'
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load data
df = pd.read_sql("SELECT * FROM churn_data", engine)

# Total customers and churn
total_customers = df.shape[0]
churned_customers = df[df['Churn'] == 1].shape[0]
churn_rate = (churned_customers / total_customers) * 100
print(f"\n Current churn rate: {churn_rate:.2f}%")

# Estimate monthly revenue loss
average_revenue = 1000
revenue_loss = average_revenue * churned_customers
print(f"Estimated current monthly revenue loss due to churn: {revenue_loss:,.0f}")

# ---- New Simulation: Top 20% at risk, retain 40% of them ----

# Assume these are top 20% high-risk (for simplicity)
top_20_percent = int(0.2 * total_customers)  # ≈192 customers
retained_customers = int(0.4 * top_20_percent)  # 40% retained → ≈77

# Revenue gain
projected_gain = retained_customers * average_revenue
churn_reduction_percent = (retained_customers / total_customers) * 100

print(f"\nHigh-risk churn group size (20%): {top_20_percent}")
print(f" Simulated churn reduction (40% retained): {churn_reduction_percent:.2f}% of all customers")
print(f" Projected monthly revenue gain: {projected_gain:,.0f}")
