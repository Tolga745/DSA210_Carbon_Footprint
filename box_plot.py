import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load data
df = pd.read_csv('commute_data.csv')

plt.figure(figsize=(8, 6))
sns.boxplot(x='traffic_condition', y='co2_emissions_kg', data=df,
            order=['low', 'moderate', 'high'],
            palette={'low': 'green', 'moderate': 'orange', 'high': 'red'})
plt.title('Carbon Emissions by Traffic Level')
plt.xlabel('Traffic Condition')
plt.ylabel('CO2 Emissions (kg)')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('emissions_boxplot.png', dpi=300)
plt.show()
