import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the commute data
df = pd.read_csv('../commute_data.csv')

# Map numeric traffic_condition values to strings
traffic_map = {0: 'low', 1: 'moderate', 2: 'high'}
df['traffic_condition'] = df['traffic_condition'].map(traffic_map)

print("\n===== HYPOTHESIS TEST 1: TRAFFIC CONDITION vs CO2 EMISSIONS =====")
print("H0: Traffic conditions have no effect on CO2 emissions")
print("H1: Different traffic conditions lead to different CO2 emission levels\n")

# Group data by traffic condition
low_traffic = df[df['traffic_condition'] == 'low']['co2_emissions_kg']
moderate_traffic = df[df['traffic_condition'] == 'moderate']['co2_emissions_kg']
high_traffic = df[df['traffic_condition'] == 'high']['co2_emissions_kg']

traffic_groups = [low_traffic, moderate_traffic, high_traffic]
traffic_labels = ['low', 'moderate', 'high']

# Check for normality in each group
print("Checking normality assumptions using Shapiro-Wilk test:")
normality_passed = True
for i, traffic_type in enumerate(traffic_labels):
    # Shapiro-Wilk test: p > 0.05 suggests normal distribution
    stat, p_value = stats.shapiro(traffic_groups[i])
    is_normal = "NORMAL" if p_value > 0.05 else "NOT NORMAL"
    print(f"  {traffic_type.capitalize()} traffic: W={stat:.4f}, p={p_value:.4f} → {is_normal}")
    if p_value <= 0.05:
        normality_passed = False

# Choose appropriate test based on normality results
print("\nSelecting appropriate statistical test:")
if normality_passed:
    # If all groups are normal, use ANOVA (parametric)
    f_stat, p_anova = stats.f_oneway(*traffic_groups)
    print(f"  Using ANOVA (parametric test for normal distributions)")
    print(f"  Result: F={f_stat:.4f}, p={p_anova:.4f}")
    significant = "SIGNIFICANT" if p_anova < 0.05 else "NOT SIGNIFICANT"
    print(f"  Conclusion: {significant} difference at α=0.05")
else:
    # If any group is not normal, use Kruskal-Wallis (non-parametric)
    stat, p_kw = stats.kruskal(*traffic_groups)
    print(f"  Using Kruskal-Wallis (non-parametric alternative to ANOVA)")
    print(f"  Result: H={stat:.4f}, p={p_kw:.4f}")
    significant = "SIGNIFICANT" if p_kw < 0.05 else "NOT SIGNIFICANT"
    print(f"  Conclusion: {significant} difference at α=0.05")