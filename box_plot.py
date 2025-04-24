import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load data
df = pd.read_csv('commute_data.csv')

# Create comparative visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Box plot comparing CO2 emissions by traffic condition
sns.boxplot(x='traffic_condition', y='co2_emissions_kg', data=df, 
            ax=axes[0, 0], order=['low', 'moderate', 'high'], palette='YlOrRd')
axes[0, 0].set_title('CO2 Emissions by Traffic Condition', fontsize=14)
axes[0, 0].set_xlabel('Traffic Condition', fontsize=12)
axes[0, 0].set_ylabel('CO2 Emissions (kg)', fontsize=12)

# Box plot comparing trip duration by traffic condition
sns.boxplot(x='traffic_condition', y='trip_duration', data=df, 
            ax=axes[0, 1], order=['low', 'moderate', 'high'], palette='YlOrRd')
axes[0, 1].set_title('Trip Duration by Traffic Condition', fontsize=14)
axes[0, 1].set_xlabel('Traffic Condition', fontsize=12)
axes[0, 1].set_ylabel('Trip Duration (minutes)', fontsize=12)

# Box plot comparing fuel efficiency by trip direction
sns.boxplot(x='trip_direction', y='fuel_efficiency_l_per_100km', data=df, ax=axes[1, 0], palette='PuBu')
axes[1, 0].set_title('Fuel Efficiency by Trip Direction', fontsize=14)
axes[1, 0].set_xlabel('Trip Direction', fontsize=12)
axes[1, 0].set_ylabel('Fuel Efficiency (L/100km)', fontsize=12)

# Box plot comparing CO2 emissions by day of week
sns.boxplot(x='day_of_week', y='co2_emissions_kg', data=df, ax=axes[1, 1], 
            order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], palette='Greens')
axes[1, 1].set_title('CO2 Emissions by Day of Week', fontsize=14)
axes[1, 1].set_xlabel('Day of Week', fontsize=12)
axes[1, 1].set_ylabel('CO2 Emissions (kg)', fontsize=12)
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('comparative_analysis.png', dpi=300)
plt.show()