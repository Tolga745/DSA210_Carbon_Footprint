import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('commute_data.csv')

# Hypothesis Test 1: Does traffic condition affect CO2 emissions?
print("Hypothesis Test: Effect of Traffic Condition on CO2 Emissions")
traffic_groups = [df[df['traffic_condition'] == cond]['co2_emissions_kg'] 
                 for cond in ['low', 'moderate', 'high']]

# Check normality assumption (if sample size permits)
for i, cond in enumerate(['low', 'moderate', 'high']):
    stat, p = stats.shapiro(traffic_groups[i])
    print(f"Shapiro-Wilk Test for {cond} traffic: W={stat:.4f}, p={p:.4f}")

# Perform ANOVA or Kruskal-Wallis test based on normality results
f_stat, p_anova = stats.f_oneway(*traffic_groups)
print(f"ANOVA test: F={f_stat:.4f}, p={p_anova:.4f}")

stat, p_kw = stats.kruskal(*traffic_groups)
print(f"Kruskal-Wallis test: H={stat:.4f}, p={p_kw:.4f}")

# Hypothesis Test 2: Does trip direction affect fuel efficiency?
print("\nHypothesis Test: Effect of Trip Direction on Fuel Efficiency")
home_to_campus = df[df['trip_direction'] == 'Home to Campus']['fuel_efficiency_l_per_100km']
campus_to_home = df[df['trip_direction'] == 'Campus to Home']['fuel_efficiency_l_per_100km']

# Check normality
stat_h2c, p_h2c = stats.shapiro(home_to_campus)
stat_c2h, p_c2h = stats.shapiro(campus_to_home)
print(f"Shapiro-Wilk Test for Home to Campus: W={stat_h2c:.4f}, p={p_h2c:.4f}")
print(f"Shapiro-Wilk Test for Campus to Home: W={stat_c2h:.4f}, p={p_c2h:.4f}")

# T-test or Mann-Whitney test
t_stat, p_ttest = stats.ttest_ind(home_to_campus, campus_to_home)
print(f"Independent t-test: t={t_stat:.4f}, p={p_ttest:.4f}")

u_stat, p_mw = stats.mannwhitneyu(home_to_campus, campus_to_home)
print(f"Mann-Whitney U test: U={u_stat:.4f}, p={p_mw:.4f}")

# Hypothesis Test 3: Correlation between trip duration and CO2 emissions
print("\nHypothesis Test: Correlation between Trip Duration and CO2 Emissions")
corr, p_corr = stats.pearsonr(df['trip_duration'], df['co2_emissions_kg'])
print(f"Pearson correlation: r={corr:.4f}, p={p_corr:.4f}")

# Spearman rank correlation (more robust to outliers and non-normality)
rho, p_spearman = stats.spearmanr(df['trip_duration'], df['co2_emissions_kg'])
print(f"Spearman correlation: ρ={rho:.4f}, p={p_spearman:.4f}")