import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load data
df = pd.read_csv('../commute_data.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])
# Extract time components
df['departure_hour'] = pd.to_datetime(df['departure_time'], format='%H:%M').dt.hour

# Basic statistics
print("Overall Statistics:")
stats_summary = df[['trip_duration', 'distance_km', 'fuel_efficiency_l_per_100km', 
                   'fuel_used_l', 'co2_emissions_kg']].describe()
print(stats_summary)

# Statistics by trip direction
print("\nStatistics by Trip Direction:")
direction_stats = df.groupby('trip_direction')[['trip_duration', 'fuel_efficiency_l_per_100km', 
                                              'co2_emissions_kg']].describe()
print(direction_stats)

# Statistics by traffic condition
print("\nStatistics by Traffic Condition:")
traffic_stats = df.groupby('traffic_condition')[['trip_duration', 'fuel_efficiency_l_per_100km', 
                                               'co2_emissions_kg']].describe()
print(traffic_stats)

# Statistics by day of week
print("\nStatistics by Day of Week:")
day_stats = df.groupby('day_of_week')[['trip_duration', 'fuel_efficiency_l_per_100km', 
                                     'co2_emissions_kg']].describe()
print(day_stats)





