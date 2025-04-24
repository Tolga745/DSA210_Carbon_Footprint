import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('commute_data.csv')

# Set up a more readable style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# Create a figure with multiple subplots for distributions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Trip duration distribution
sns.histplot(df['trip_duration'], kde=True, ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('Distribution of Trip Duration', fontsize=14)
axes[0, 0].set_xlabel('Duration (minutes)', fontsize=12)
axes[0, 0].set_ylabel('Frequency', fontsize=12)

# Fuel efficiency distribution
sns.histplot(df['fuel_efficiency_l_per_100km'], kde=True, ax=axes[0, 1], color='forestgreen')
axes[0, 1].set_title('Distribution of Fuel Efficiency', fontsize=14)
axes[0, 1].set_xlabel('Fuel Efficiency (L/100km)', fontsize=12)
axes[0, 1].set_ylabel('Frequency', fontsize=12)

# CO2 emissions distribution
sns.histplot(df['co2_emissions_kg'], kde=True, ax=axes[1, 0], color='darkred')
axes[1, 0].set_title('Distribution of CO2 Emissions', fontsize=14)
axes[1, 0].set_xlabel('CO2 Emissions (kg)', fontsize=12)
axes[1, 0].set_ylabel('Frequency', fontsize=12)

# Distance distribution
sns.histplot(df['distance_km'], kde=True, ax=axes[1, 1], color='purple')
axes[1, 1].set_title('Distribution of Trip Distance', fontsize=14)
axes[1, 1].set_xlabel('Distance (km)', fontsize=12)
axes[1, 1].set_ylabel('Frequency', fontsize=12)

plt.tight_layout()
plt.savefig('distribution_analysis.png', dpi=300)
plt.show()