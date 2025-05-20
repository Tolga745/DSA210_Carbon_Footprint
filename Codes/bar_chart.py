import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('../commute_data.csv')

traffic_mapping = {'low': 0, 'moderate': 1, 'high': 2}
df['traffic_condition'] = df['traffic_condition'].replace(traffic_mapping)

# Convert to numeric type to ensure calculations work properly
df['traffic_condition'] = pd.to_numeric(df['traffic_condition'], errors='coerce')
df['co2_emissions_kg'] = pd.to_numeric(df['co2_emissions_kg'], errors='coerce')

# Create traffic condition labels for better readability
traffic_labels = {0: 'Low Traffic (0)', 1: 'Moderate Traffic (1)', 2: 'High Traffic (2)'}

# Set up the figure
plt.figure(figsize=(12, 7))

# Create bins for the histogram
bins = np.linspace(df['co2_emissions_kg'].min(), df['co2_emissions_kg'].max(), 10)

# Create a true histogram
plt.hist([
    df[df['traffic_condition'] == 0]['co2_emissions_kg'],
    df[df['traffic_condition'] == 1]['co2_emissions_kg'],
    df[df['traffic_condition'] == 2]['co2_emissions_kg']
], 
    bins=bins, 
    label=[traffic_labels[0], traffic_labels[1], traffic_labels[2]],
    color=['green', 'orange', 'red'],
    alpha=0.7,
    stacked=True  # This creates a stacked histogram
)

# Add a vertical line for the overall average
plt.axvline(x=df['co2_emissions_kg'].mean(), color='blue', linestyle='--', linewidth=1.5, 
           label=f'Overall Mean: {df["co2_emissions_kg"].mean():.2f} kg')

# Calculate average for each traffic condition
for traffic, color in zip([0, 1, 2], ['green', 'orange', 'red']):
    subset = df[df['traffic_condition'] == traffic]
    if not subset.empty:
        avg = subset['co2_emissions_kg'].mean()
        plt.axvline(x=avg, color=color, linestyle=':', linewidth=1.5,
                   label=f'{traffic_labels[traffic]} Mean: {avg:.2f} kg')

# Add labels and title
plt.xlabel('CO2 Emissions (kg)', fontsize=12)
plt.ylabel('Frequency (Number of Trips)', fontsize=12)
plt.title('Histogram of CO2 Emissions by Traffic Condition', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Add summary statistics as text
traffic_counts = df.groupby('traffic_condition')['co2_emissions_kg'].count()
traffic_means = df.groupby('traffic_condition')['co2_emissions_kg'].mean()

stats_text = (
    f"Data Summary:\n"
    f"Low Traffic (0): {traffic_counts.get(0, 0)} trips, avg: {traffic_means.get(0, 0):.2f} kg CO2\n"
    f"Moderate Traffic (1): {traffic_counts.get(1, 0)} trips, avg: {traffic_means.get(1, 0):.2f} kg CO2\n"
    f"High Traffic (2): {traffic_counts.get(2, 0)} trips, avg: {traffic_means.get(2, 0):.2f} kg CO2\n"
    f"Overall: {len(df)} trips, avg: {df['co2_emissions_kg'].mean():.2f} kg CO2"
)
plt.figtext(0.5, 0.01, stats_text, ha='center', fontsize=10, 
            bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout(rect=[0, 0.08, 1, 0.95])

# Show the plot
plt.show()