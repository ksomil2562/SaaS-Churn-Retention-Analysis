import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:somilkumar@localhost:5432/saas_churn_project')

# Load data
df = pd.read_sql('SELECT * FROM churn_data', engine)

# Set plot style
sns.set(style="whitegrid")

# List of important numeric columns
num_cols = [
    'MonthlyCharges', 'TotalCharges', 'ViewingHoursPerWeek',
    'AverageViewingDuration', 'ContentDownloadsPerMonth',
    'UserRating', 'WatchlistSize', 'SupportTicketsPerMonth'
]

for col in num_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x='Churn', y=col, data=df)
    plt.title(f'{col} vs Churn')
    plt.tight_layout()
    plt.show()
