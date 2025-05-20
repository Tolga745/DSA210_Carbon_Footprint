import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Assume the data is loaded from a CSV file
# Instead of hardcoding the entire dataset, we'll use this approach:
df = pd.read_csv('../commute_data.csv')  # Replace with your actual file path

traffic_mapping = {0: 'Low', 1: 'Moderate', 2: 'High'}
df['traffic_category'] = df['traffic_condition'].map(traffic_mapping)

# Create a figure with multiple subplots
fig, axes = plt.subplots(figsize=(7, 5))

# Color mapping for consistency
color_mapping = {'Low': 'green', 'Moderate': 'orange', 'High': 'red'}

# 1. Trip Duration Distribution - Histogram
# 2. Fuel Consumption Distribution - Histogram
sns.histplot(data=df, x='fuel_used_l',  
             bins=10, kde=True, palette=color_mapping,
             ax=axes)
axes.set_title('Distribution of Fuel Consumption')
axes.set_xlabel('Fuel Used (liters)')
axes.set_ylabel('Frequency')




print("\nSummary Statistics for Fuel Consumption (liters):")
fuel_stats = df.groupby('traffic_category')['fuel_used_l'].describe().round(2)
# Reorder to have Low, Moderate, High sequence
fuel_stats = fuel_stats.reindex(['Low', 'Moderate', 'High'])
print(fuel_stats)

# Optional: Calculate correlations
print("\nCorrelation between Trip Duration and Fuel Consumption:")
print(df[['trip_duration', 'fuel_used_l', 'distance_km', 'fuel_efficiency_l_per_100km']].corr().round(3))

plt.show()