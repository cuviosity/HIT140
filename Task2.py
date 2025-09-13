import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
from scipy import stats

# Loading of datasets
df = pd.read_csv("dataset2.csv")
df['rat_present'] = (df['rat_minutes'] > 0).astype(int)

# Defining of seasons
def assign_seas(month) :
     if month in [12, 1, 2]:
       return 'Winter'
     elif month in [3, 4, 5,]:
       return 'Spring'
     elif month in [6, 7, 8]:
        return 'Summer'
     else:
        return 'Autumn'
df['season'] = df['month'].apply(assign_seas)

# Set up of plotting style
plt.style.use('seaborn-v0_8')
fig = plt.figure(figsize=(12, 8))

# Investigation A - Box plot comparing the bats behaviour with/without rats
plt.subplot(2, 3, 1)
box_data = [
     df[df['rat_present'] == 0]['bat_landing_number'],
     df[df['rat_present'] == 1]['bat_landing_number'],
] 
plt.boxplot(box_data, tick_labels=['Rat Absent', 'Rats Present'])
plt.title('Bat Landing Behaviour\nby Rat Presense')
plt.ylabel('Bat Landing Number')
plt.grid(True, alpha=0.3)

# Adding of sample sizes
n_absent = len(df[df['rat_present'] == 0])
n_present = len(df[df['rat_present'] == 1])
plt.text(1, plt.ylim()[1]*0.9, f'n={n_absent}', ha='center', fontsize=10)
plt.text(2, plt.ylim()[1]*0.9, f'n={n_present}', ha='center', fontsize=10)

# Histogram comparison
plt.subplot(2, 3, 2)
plt.hist(df[df['rat_present'] == 0]['bat_landing_number'],
        alpha=0.7, label='Rat Absent', bins=20, color='skyblue')
plt.hist(df[df['rat_present'] == 1]['bat_landing_number'],
        alpha=0.7, label='Rats Present', bins=20, color='orange')
plt.xlabel('Bat Landing Number')
plt.ylabel('Frequency')
plt.title('Distribution of Bat Landings')
plt.legend()
plt.grid(True)

# Investigation B - Seasonal Comparison
plt.subplot(2, 3, 3,)
season_order = ['Spring', 'Summer', 'Autumn', 'Winter']
season_in_data = [s for s in season_order if s in df['season'].values]
sns.boxplot(data=df, x='season', y='bat_landing_number', order=['Spring', 'Summer', 'Autumn', 'Winter'])
plt.title('Seasonal Bat Behaviour')
plt.ylabel('Number of Bat Lnadings')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

#Correlation Heatmap
plt.subplot(2, 3, 4)
correlation_vars = ['bat_landing_number', 'rat_minutes', 'rat_arrival_number',
                    'food_availability', 'hours_after_sunset', 'month']
corr_matrix = df[correlation_vars].corr()
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', center=0,
            square=True, fmt='.2f', cbar_kws={'label': 'Correlations'})
plt.title('Variable Correlations')
plt.tight_layout()

# Scatter plot of Rat activity vs bat behaviour
plt.subplot(2, 3, 5)
plt.scatter(df['rat_minutes'], df['bat_landing_number'], alpha=0.5, s=20)
plt.xlabel('Rat Minutes Present')
plt.ylabel('Bat Landing Number')
plt.title('Rat Activity vs Bat Behaviour')

#Adding trend line
z = np.polyfit(df['rat_minutes'], df['bat_landing_number'], 1)
p = np.poly1d(z)
plt.plot(df['rat_minutes'], p(df['rat_minutes']), "r--", alpha=0.8)

# Calculate and display correlation
corr_coef = df['rat_minutes'].corr(df['bat_landing_number'])
plt.text(0.5, 0.95, f'r = {corr_coef:.3f}', transform=plt.gca().transAxes)
plt.grid(True)

# Monthly patterns
plt.subplot(2, 3, 6)
monthly_bat = df.groupby('month')['bat_landing_number'].mean()
monthly_rat = df.groupby('month')['rat_minutes'].mean()

ax1= plt.gca()
ax1.plot(monthly_bat.index, monthly_bat.values, 'b-o', label='Bat Landings', linewidth=2)
ax1.set_xlabel('Month')
ax1.set_ylabel('Average Bat Landings', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(monthly_rat.index, monthly_rat.values, 'r-s', label='Rat Minutes', linewidth=2)
ax2.set_ylabel('Average Rat Minutes', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('MOnthly Patterns: Bat vs Rats')
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels(['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])

plt.tight_layout()
plt.show()

# Histogram of number of bat landings 
plt.hist(df["bat_landing_number"], bins=30, color="skyblue", edgecolor="black")
plt.title("Number of Bat Landing")
plt.xlabel("Number of Landings")
plt.ylabel("How Frequent")
plt.show()

