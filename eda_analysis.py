import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# PostgreSQL connection
username = 'postgres'
password = 'somilkumar'
host = 'localhost'
port = '5432'
database = 'saas_churn_project'
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Load cleaned data
df = pd.read_sql("SELECT * FROM churn_data", engine)

# Make sure columns are lowercase
df.columns = df.columns.str.lower()

# Convert churn column to binary
df['churn'] = df['churn'].astype(int)

# Set visual style
sns.set(style="whitegrid")


# Churn rate %
churn_rate = df['churn'].mean() * 100
print(f"Overall churn rate: {churn_rate:.2f}%")

# Bar plot of churn
sns.countplot(x='churn', data=df)
plt.title("Customer Churn Count (0 = Retained, 1 = Churned)")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()
