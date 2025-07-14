import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:somilkumar@localhost:5432/saas_churn_project')

# Load data
df = pd.read_sql('SELECT * FROM churn_data', engine)

# Convert Churn to int (if not already)
df['Churn'] = df['Churn'].astype(int)

# Set plot style
sns.set(style="whitegrid")

# 1. Viewing Hours per Week vs Churn
plt.figure(figsize=(7, 4))
sns.boxplot(x='Churn', y='ViewingHoursPerWeek', data=df)
plt.title('Viewing Hours per Week by Churn')
plt.xticks([0, 1], ['Retained', 'Churned'])
plt.tight_layout()
plt.show()

# 2. User Rating vs Churn
plt.figure(figsize=(7, 4))
sns.boxplot(x='Churn', y='UserRating', data=df)
plt.title('User Rating by Churn')
plt.xticks([0, 1], ['Retained', 'Churned'])
plt.tight_layout()
plt.show()

# 3. SubscriptionType vs Churn
plt.figure(figsize=(7, 4))
sns.countplot(x='SubscriptionType', hue='Churn', data=df)
plt.title('Churn Count by Subscription Type')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 4. PaymentMethod vs Churn
plt.figure(figsize=(7, 4))
sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.title('Churn by Payment Method')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
