import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:somilkumar@localhost:5432/saas_churn_project')

# Load data
df = pd.read_sql('SELECT * FROM churn_data', engine)

# Encode churn as numeric if it's not already (optional step)
df['Churn'] = df['Churn'].astype(int)

# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Compute correlation matrix
corr_matrix = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numeric Features')
plt.tight_layout()
plt.show()
