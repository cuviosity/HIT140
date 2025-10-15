import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import datetime

df = pd.read_csv('dataset1.csv')

date_cols = ['start_time', 'rat_period_start', 'rat_period_end', 'sunset_time']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y %H:%M', errors='coerce')

numeric_cols = ['bat_landing_to_food', 'seconds_after_rat_arrival', 'risk', 'reward', 'month', 'hours_after_sunset', 'season']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['habit'] = df['habit'].replace('', np.nan).replace(r'^\s*$', np.nan, regex=True)

print("Initial Data Summary:")
print(df.describe(include='all'))
print("\nMissing Values Count:")
print(df.isnull().sum())

key_cols = ['season', 'bat_landing_to_food', 'risk', 'reward', 'habit']
df_clean = df.dropna(subset=key_cols)
print(f"\nRows after dropping NaNs in key columns: {len(df_clean)}")

df_clean['rat_encounter'] = df_clean['habit'].str.contains('rat', case=False, na=False).astype(int)

df_clean['time_of_day'] = pd.cut(df_clean['hours_after_sunset'], bins=[0, 3, 6, 9, 12, np.inf], labels=['Early Evening', 'Evening', 'Night', 'Late Night', 'Dawn'])

print("\nSummary Stats by Season:")
grouped = df_clean.groupby('season')
print(grouped[['bat_landing_to_food', 'risk', 'reward', 'rat_encounter', 'hours_after_sunset']].mean())

df_clean.to_csv('processed_dataset1.csv', index=False)
print("\nProcessed data saved to 'processed_dataset1.csv'")

season0_time = df_clean[df_clean['season'] == 0]['bat_landing_to_food'].dropna()
season1_time = df_clean[df_clean['season'] == 1]['bat_landing_to_food'].dropna()
if len(season0_time) > 1 and len(season1_time) > 1:
    t_stat_time, p_val_time = stats.ttest_ind(season0_time, season1_time)
    print(f"\nt-test for bat_landing_to_food: t={t_stat_time:.2f}, p={p_val_time:.4f}")
    if p_val_time < 0.05:
        print("Significant difference: Bats approach food faster in one season (check means).")
else:
    print("\nInsufficient data for t-test on bat_landing_to_food.")

contingency_risk = pd.crosstab(df_clean['season'], df_clean['risk'])
chi2_risk, p_risk, _, _ = stats.chi2_contingency(contingency_risk)
print(f"Chi-square for risk vs. season: chi2={chi2_risk:.2f}, p={p_risk:.4f}")
if p_risk < 0.05:
    print("Significant: Risk-taking changes with season.")

contingency_reward = pd.crosstab(df_clean['season'], df_clean['reward'])
chi2_reward, p_reward, _, _ = stats.chi2_contingency(contingency_reward)
print(f"Chi-square for reward vs. season: chi2={chi2_reward:.2f}, p={p_reward:.4f}")
if p_reward < 0.05:
    print("Significant: Rewarding behavior changes with season.")

contingency_rat = pd.crosstab(df_clean['season'], df_clean['rat_encounter'])
chi2_rat, p_rat, _, _ = stats.chi2_contingency(contingency_rat)
print(f"Chi-square for rat_encounter vs. season: chi2={chi2_rat:.2f}, p={p_rat:.4f}")
if p_rat < 0.05:
    print("Significant: Rat encounters more frequent in spring.")

top_habits = df_clean['habit'].value_counts().head(5).index
df_habits = df_clean[df_clean['habit'].isin(top_habits)]
if len(top_habits) > 1:
    contingency_habit = pd.crosstab(df_habits['season'], df_habits['habit'])
    chi2_habit, p_habit, _, _ = stats.chi2_contingency(contingency_habit)
    print(f"Chi-square for habits vs. season: chi2={chi2_habit:.2f}, p={p_habit:.4f}")
    if p_habit < 0.05:
        print("Significant: Behavior habits change with season.")
else:
    print("\nInsufficient habits for chi-square test.")
