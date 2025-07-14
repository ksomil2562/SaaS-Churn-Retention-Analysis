import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:somilkumar@localhost:5432/saas_churn_project')

# Load data
df = pd.read_sql('SELECT * FROM churn_data', engine)

# Clean column names if needed
df.columns = df.columns.str.strip()

# List of important categorical variables
cat_vars = ['SubscriptionType', 'PaymentMethod', 'ContentType', 'MultiDeviceAccess', 'ParentalControl', 'SubtitlesEnabled']

# Set plot style
sns.set(style="whitegrid")

for col in cat_vars:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, hue='Churn')
    plt.title(f'Churn by {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
