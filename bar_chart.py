import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('commute_data.csv')

traffic_mapping = {'low': 0, 'moderate': 1, 'high': 2}
df['traffic_condition'] = df['traffic_condition'].replace(traffic_mapping)

# Convert to numeric type to ensure calculations work properly
df['traffic_condition'] = pd.to_numeric(df['traffic_condition'], errors='coerce')
df['co2_emissions_kg'] = pd.to_numeric(df['co2_emissions_kg'], errors='coerce')

# Create traffic condition labels for better readability
traffic_labels = {0: 'Low', 1: 'Moderate', 2: 'High'}

# Group data by traffic condition
grouped_data = df.groupby('traffic_condition')['co2_emissions_kg']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 1. Histogram of CO2 emissions separated by traffic condition
for traffic_level, color in zip([0, 1, 2], ['green', 'orange', 'red']):
    subset = df[df['traffic_condition'] == traffic_level]['co2_emissions_kg']
    if not subset.empty:
        ax1.hist(subset, alpha=0.6, bins=8, label=traffic_labels[traffic_level], color=color)

ax1.set_title('CO2 Emissions Distribution by Traffic Condition', fontsize=14)
ax1.set_xlabel('CO2 Emissions (kg)', fontsize=12)
ax1.set_ylabel('Frequency (Number of Trips)', fontsize=12)
ax1.legend(title='Traffic Condition')
ax1.grid(True, alpha=0.3)

# 2. Bar chart showing average CO2 emissions by traffic condition
mean_emissions = grouped_data.mean().reindex([0, 1, 2])
std_emissions = grouped_data.std().reindex([0, 1, 2])

colors = ['green', 'orange', 'red']
bars = ax2.bar(
    [traffic_labels[i] for i in mean_emissions.index],
    mean_emissions.values,
    yerr=std_emissions.values,
    capsize=10,
    color=colors
)

# Add the value labels on top of each bar
for bar, value in zip(bars, mean_emissions.values):
    ax2.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.1,
        f'{value:.2f} kg',
        ha='center',
        fontsize=10
    )

ax2.set_title('Average CO2 Emissions by Traffic Condition', fontsize=14)
ax2.set_xlabel('Traffic Condition', fontsize=12)
ax2.set_ylabel('Average CO2 Emissions (kg)', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')

# Some additional statistics to display in the plot
counts = grouped_data.count().reindex([0, 1, 2])
stats_text = (
    f"Data Summary:\n"
    f"Low Traffic: {counts[0]} trips, avg: {mean_emissions[0]:.2f} kg CO2\n"
    f"Moderate Traffic: {counts[1]} trips, avg: {mean_emissions[1]:.2f} kg CO2\n"
    f"High Traffic: {counts[2]} trips, avg: {mean_emissions[2]:.2f} kg CO2"
)
fig.text(0.5, 0.01, stats_text, ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.suptitle('Analysis of CO2 Emissions vs. Traffic Conditions', fontsize=16)
plt.subplots_adjust(top=0.9, bottom=0.15)

# Display the plot
plt.show()

# Print additional statistics
print("\nStatistical Summary by Traffic Condition:")
print(grouped_data.agg(['count', 'mean', 'median', 'min', 'max', 'std']).round(3))