import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('commute_data.csv')

# Map traffic condition numbers to labels
traffic_map = {0: 'low', 1: 'moderate', 2: 'high'}
df['traffic_condition'] = df['traffic_condition'].map(traffic_map)

# Set categorical order for consistent coloring
df['traffic_condition'] = pd.Categorical(df['traffic_condition'],
                                         categories=['low', 'moderate', 'high'],
                                         ordered=True)

# Plot
sns.set(style='whitegrid')
scatter = sns.lmplot(
    x='trip_duration',
    y='co2_emissions_kg',
    hue='traffic_condition',
    data=df,
    palette={'low': 'green', 'moderate': 'orange', 'high': 'red'},
    height=6,
    aspect=1.5,
    scatter_kws={'s': 70, 'alpha': 0.6}
)

# Titles and labels
scatter.set(title='Traffic Impact on Carbon Emissions')
scatter.set_axis_labels('Trip Duration (minutes)', 'CO2 Emissions (kg)')

# Optional annotation
plt.annotate(
    'Higher traffic = More emissions',
    xy=(df['trip_duration'].max() * 0.6, df['co2_emissions_kg'].max() * 0.7),
    xytext=(df['trip_duration'].max() * 0.7, df['co2_emissions_kg'].max() * 0.85),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12
)

plt.tight_layout()
plt.savefig('traffic_vs_emissions.png', dpi=300, bbox_inches='tight')
plt.show()
