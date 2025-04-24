import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('commute_data.csv')

# Create scatter plot with regression lines
plt.figure(figsize=(10, 6))
scatter = sns.lmplot(x='trip_duration', y='co2_emissions_kg', 
                     hue='traffic_condition', data=df,
                     palette={'low':'green', 'moderate':'orange', 'high':'red'},
                     height=6, aspect=1.5, scatter_kws={'s':80, 'alpha':0.7})

# Customize plot appearance
plt.title('Traffic Impact on Carbon Emissions', fontsize=16, pad=20)
plt.xlabel('Trip Duration (minutes)', fontsize=12)
plt.ylabel('CO2 Emissions (kg)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

# Add annotation for traffic trend
plt.annotate('Higher traffic = More emissions', 
             xy=(70, 4.5), xytext=(80, 5.0),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12)

plt.tight_layout()
plt.savefig('traffic_vs_emissions.png', dpi=300, bbox_inches='tight')
plt.show()